# Agentic4API — Devoteam nexDigital

> Plateforme d'agents AI pour la découverte et la génération de contrats d'APIs d'entreprise.

Projet réalisé dans le cadre d'un stage **Consultant AI & Architecture** chez **Devoteam nexDigital**.

---

## Présentation

Agentic4API est une plateforme composée de deux agents AI autonomes :

- **Agent Discovery** — trouve les APIs existantes dans un catalogue via recherche sémantique (Pinecone + Mistral embeddings)
- **Agent Architect** — génère des contrats OpenAPI 3.0 complets à partir d'un besoin exprimé en langage naturel

Tous les appels LLM et outils transitent par **Kong Gateway**, qui joue le rôle de point d'entrée unique sécurisé pour l'ensemble de la plateforme.

---

## Architecture

```
Client (navigateur / n8n Chat)
         │
         ▼
    ┌─────────────────────────────────┐
    │         Kong Gateway :8000      │
    │   Key Auth + Request Transformer│
    │                                 │
    │  /llm  ──────────────────────── │──► Mistral Cloud API
    │  /mcp  ──────────────────────── │──► MCP Server :3000
    └─────────────────────────────────┘
                                           │
                              ┌────────────┼────────────────┐
                              ▼            ▼                 ▼
                     /tools/search_apis  /tools/        /tools/
                        Pinecone       get_naming_    generate_openapi
                     (recherche        standards        Mistral LLM
                     sémantique)

    ┌─────────────────────────────────┐
    │           n8n :5678             │
    │   Agent Discovery               │
    │   Agent Architect               │
    │   OpenAI Chat Model             │
    │   → Base URL: kong:8000/llm/v1  │
    └─────────────────────────────────┘
```

---

## Stack technique

| Composant | Technologie | Rôle |
|---|---|---|
| Orchestrateur | n8n (Docker) | Workflow des agents AI |
| API Gateway | Kong Gateway 3.6 | Routage, auth, proxy LLM |
| LLM | Mistral Cloud API | Chat + embeddings |
| Recherche sémantique | Pinecone | Index vectoriel des APIs |
| MCP Server | Node.js / Express | Outils appelés par les agents |
| Base de données Kong | PostgreSQL 15 | Persistance config Kong |
| UI Kong | Kong Manager :8002 | Administration visuelle |

---

## Prérequis

- Docker Desktop installé et en cours d'exécution
- Une clé API Mistral valide → [console.mistral.ai](https://console.mistral.ai)
- Un index Pinecone nommé `api-discovery` avec des embeddings de dimension 1024 → [app.pinecone.io](https://app.pinecone.io)

---

## Installation

### 1. Cloner le projet

```bash
git clone <url-du-repo>
cd agentic4api
```

### 2. Configurer les variables d'environnement

```bash
cp .env.example .env
```

Édite `.env` et renseigne tes clés :

```env
MISTRAL_API_KEY=sk-...
PINECONE_API_KEY=pcsk_...
PINECONE_INDEX_HOST=https://api-discovery-xxxx.svc.aped-xxxx.pinecone.io
KONG_INTERNAL_KEY=n8n-internal-key-2025
N8N_BASIC_AUTH_USER=admin
N8N_BASIC_AUTH_PASSWORD=admin123
```

### 3. Démarrer les containers

```bash
docker compose up -d --build
```

Attends que tous les containers soient `healthy` (environ 30 secondes) :

```bash
docker compose ps
```

### 4. Configurer Kong

```powershell
.\kong-setup.ps1
```

Ce script configure automatiquement :
- Services `mistral-llm` et `mcp-server`
- Routes `/llm` et `/mcp`
- Plugin Key Auth sur les deux services
- Plugin Request Transformer (injection clé Mistral)
- Consumer `n8n-agent` avec sa clé interne

### 5. Accéder aux interfaces

| Interface | URL | Identifiants |
|---|---|---|
| n8n (agents) | http://localhost:5678 | admin / admin123 |
| Kong Manager | http://localhost:8002 | — |
| MCP Server health | http://localhost:3000/health | — |

---

## Tests de validation

```powershell
# 1. MCP Server direct
Invoke-RestMethod -Uri "http://localhost:3000/health"

# 2. Kong → MCP
Invoke-RestMethod -Uri "http://localhost:8000/mcp/health" `
  -Headers @{ "apikey" = "n8n-internal-key-2025" }

# 3. Kong → Mistral
Invoke-RestMethod -Method POST "http://localhost:8000/llm/v1/chat/completions" `
  -Headers @{ "apikey" = "n8n-internal-key-2025"; "Content-Type" = "application/json" } `
  -Body '{"model":"mistral-small-latest","messages":[{"role":"user","content":"hello"}]}'

# 4. Recherche sémantique Pinecone
Invoke-RestMethod -Method POST "http://localhost:8000/mcp/tools/search_apis" `
  -Headers @{ "apikey" = "n8n-internal-key-2025"; "Content-Type" = "application/json" } `
  -Body '{"query":"API de paiement"}'
```

---

## Outils MCP disponibles

### `POST /tools/search_apis`

Recherche sémantique dans le catalogue Pinecone.

```json
{ "query": "API de gestion des paiements" }
```

### `GET /tools/get_naming_standards`

Retourne les standards de nommage Devoteam nexDigital.

### `POST /tools/generate_openapi`

Génère un contrat OpenAPI 3.0 complet.

```json
{ "description": "API de gestion des commandes e-commerce" }
```

---

## Configuration Kong

### Services

| Nom | URL | Description |
|---|---|---|
| `mistral-llm` | https://api.mistral.ai:443/ | Proxy vers Mistral Cloud |
| `mcp-server` | http://mcp-server:3000 | Outils agents (MCP) |

### Routes

| Route | Path | Strip path | Service |
|---|---|---|---|
| `llm-route` | `/llm` | true | mistral-llm |
| `mcp-route` | `/mcp` | true | mcp-server |

### Plugins actifs

| Plugin | Service | Rôle |
|---|---|---|
| `key-auth` | mistral-llm | Authentification interne |
| `key-auth` | mcp-server | Authentification interne |
| `request-transformer` | mistral-llm | Injection `Authorization: Bearer <MISTRAL_KEY>` |

### Consumer

| Username | Clé | Utilisé par |
|---|---|---|
| `n8n-agent` | `n8n-internal-key-2025` | n8n (agents AI) |

---

## Structure du projet

```
agentic4api/
├── .env                    ← Variables d'environnement (non versionné)
├── .env.example            ← Template des variables
├── docker-compose.yml      ← Stack complète
├── kong-setup.ps1          ← Script de configuration Kong
├── kong/                   ← (réservé pour configs Kong déclaratives)
├── mcp-server/
│   ├── Dockerfile
│   ├── package.json
│   └── server.js           ← Serveur Express avec les 3 outils
└── n8n/
    └── workflows/          ← Exports JSON des agents n8n
```

---

## Dépannage

### Kong ne démarre pas (`New migrations available`)

```powershell
docker run --rm --network agentic4api_ai-network `
  -e KONG_DATABASE=postgres -e KONG_PG_HOST=kong-db `
  -e KONG_PG_USER=kong -e KONG_PG_PASSWORD=kong -e KONG_PG_DATABASE=kong `
  kong/kong-gateway:3.6 kong migrations up

docker run --rm --network agentic4api_ai-network `
  -e KONG_DATABASE=postgres -e KONG_PG_HOST=kong-db `
  -e KONG_PG_USER=kong -e KONG_PG_PASSWORD=kong -e KONG_PG_DATABASE=kong `
  kong/kong-gateway:3.6 kong migrations finish

docker compose up -d kong
```

### MCP Server retourne `fetch failed`

Vérifier que `PINECONE_INDEX_HOST` dans `.env` est correct, puis forcer la recréation :

```powershell
docker compose stop mcp-server
docker compose rm -f mcp-server
docker compose up -d mcp-server
```

### Mistral retourne `429 capacity exceeded`

Le free tier Mistral est limité. Attendre 60 secondes entre les requêtes ou passer à un plan payant.

### n8n retourne `401` vers Kong

Vérifier que le Custom Header `apikey: n8n-internal-key-2025` est bien configuré dans la credential OpenAI de n8n (Add Custom Header → activé).

---

## Auteur

**Salmane El Hajouji** — Stagiaire Consultant AI & Architecture  
Devoteam nexDigital — 2026