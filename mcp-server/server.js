// ─────────────────────────────────────────────────────────────────
// MCP Server — Agentic4API
// Serveur Express custom exposant les outils utilisés par les agents AI
// Tous les appels transitent via Kong Gateway (/mcp)
// ─────────────────────────────────────────────────────────────────

const express = require("express");
const app = express();
app.use(express.json()); // Permet de lire le body JSON des requêtes POST

// ── Configuration ─────────────────────────────────────────────────
// Les clés sont injectées par Docker depuis le fichier .env
// Elles ne sont jamais écrites en dur dans le code
const PORT = process.env.PORT || 3000;
const PINECONE_API_KEY = process.env.PINECONE_API_KEY;     // Clé d'accès Pinecone
const PINECONE_INDEX_HOST = process.env.PINECONE_INDEX_HOST; // URL de l'index vectoriel
const MISTRAL_API_KEY = process.env.MISTRAL_API_KEY;       // Clé Mistral pour les embeddings

// ── Health Check ──────────────────────────────────────────────────
// Endpoint appelé par Docker et Kong pour vérifier que le serveur est vivant
// Si pas de réponse → Docker redémarre le container automatiquement
app.get("/health", (req, res) => {
  res.json({ status: "ok", timestamp: new Date().toISOString() });
});

// ── Tool : search_apis ────────────────────────────────────────────
// Outil principal de l'Agent Discovery
// Reçoit une query en langage naturel et retourne les APIs les plus pertinentes
// Flux : query texte → vecteur Mistral → recherche Pinecone → résultats scorés
app.post("/tools/search_apis", async (req, res) => {
  try {
    // Récupération de la query envoyée par l'agent n8n
    const { query } = req.body;

    // Validation : la query est obligatoire
    if (!query) return res.status(400).json({ error: "query is required" });

    // ── ÉTAPE 1 : Conversion texte → vecteur (Mistral Embeddings) ──
    // Mistral transforme la query en un tableau de 1024 nombres
    // Ex: "API de paiement" → [-0.031, 0.024, 0.028, ...]
    // Deux textes au sens proche auront des vecteurs mathématiquement proches
    const embedRes = await fetch("https://api.mistral.ai/v1/embeddings", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        Authorization: `Bearer ${MISTRAL_API_KEY}`,
      },
      body: JSON.stringify({
        model: "mistral-embed", // Modèle d'embedding Mistral (1024 dims)
        input: [query],         // On passe la query dans un tableau
      }),
    });

    const embedData = await embedRes.json();

    // Vérification que Mistral a bien retourné un embedding
    if (!embedData.data) {
      return res.status(500).json({ error: "Mistral embed failed", detail: embedData });
    }

    // Extraction du vecteur (tableau de 1024 floats)
    const vector = embedData.data[0].embedding;

    // ── ÉTAPE 2 : Recherche sémantique dans Pinecone ──────────────
    // On envoie le vecteur à Pinecone qui compare avec toutes les APIs indexées
    // et retourne les 5 plus proches (topK=5) avec leur score de similarité
    // Score proche de 1.0 = très pertinent / proche de 0 = peu pertinent
    const pineconeRes = await fetch(`${PINECONE_INDEX_HOST}/query`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "Api-Key": PINECONE_API_KEY,
      },
      body: JSON.stringify({
        vector,              // Le vecteur généré par Mistral
        topK: 5,             // Nombre max de résultats retournés
        includeMetadata: true, // Inclure les métadonnées (nom, description, endpoints)
      }),
    });

    const pineconeData = await pineconeRes.json();

    // ── ÉTAPE 3 : Formatage et retour des résultats ───────────────
    // On retourne uniquement les champs utiles pour l'agent :
    // - id       : identifiant unique de l'API dans Pinecone
    // - score    : score de similarité (0 à 1) — ex: 0.87 = très pertinent
    // - metadata : nom, description, endpoints de l'API
    res.json({
      results: pineconeData.matches.map((m) => ({
        id: m.id,
        score: m.score,
        metadata: m.metadata,
      })),
    });

  } catch (err) {
    // Gestion des erreurs réseau ou inattendues
    console.error("search_apis error:", err);
    res.status(500).json({ error: err.message });
  }
});

// ── Démarrage du serveur ──────────────────────────────────────────
app.listen(PORT, () =>
  console.log(`MCP Server running on port ${PORT}`)
);