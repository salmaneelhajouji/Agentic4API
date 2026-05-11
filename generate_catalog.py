# generate_catalog.py — à mettre à la racine de ton projet Agentic4API

import json
import os

API_FOLDER = "api-catalogue"  # chemin relatif depuis la racine
OUTPUT_FILE = "catalog.json"

catalog = []
errors = []

files = [f for f in os.listdir(API_FOLDER) if f.endswith(".json")]
print(f"{len(files)} fichiers trouvés")

for filename in sorted(files):
    filepath = os.path.join(API_FOLDER, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = json.load(f)

        info = content.get("info", {})

        # Extrait les summaries d'endpoints uniquement
        endpoints = []
        for path, methods in content.get("paths", {}).items():
            for method, details in methods.items():
                if method in ["get", "post", "put", "delete", "patch"]:
                    summary = details.get("summary", "")
                    if summary:
                        endpoints.append(f"{method.upper()} {path} — {summary}")

        catalog.append({
            "name": info.get("x-api-id", filename.replace(".json", "")),
            "title": info.get("title", ""),
            "version": info.get("x-api-version", "v1"),
            "status": info.get("x-status", "active"),
            "domain": info.get("x-domain", ""),
            "team": info.get("x-team", ""),
            "description": info.get("description", ""),
            "endpoints": endpoints[:5]
        })

    except Exception as e:
        errors.append(filename)
        print(f"  ⚠ Erreur : {filename} → {e}")

# ── Stats ──────────────────────────────────────────────────────────────────
print(f"\n✅ {len(catalog)} APIs consolidées")
print(f"❌ {len(errors)} erreurs : {errors}")

# ── Sauvegarde ─────────────────────────────────────────────────────────────
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    json.dump(catalog, f, ensure_ascii=False, indent=2)

size_kb = os.path.getsize(OUTPUT_FILE) / 1024
print(f"\n📦 {OUTPUT_FILE} : {size_kb:.1f} KB")
print(f"📊 Estimation tokens : ~{int(size_kb * 200)} tokens")

# ── Aperçu du premier élément ──────────────────────────────────────────────
print("\nExemple (1ère API) :")
print(json.dumps(catalog[0], ensure_ascii=False, indent=2))