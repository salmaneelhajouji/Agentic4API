# convert_apis_for_vertex.py
# Lance depuis la racine du projet : python convert_apis_for_vertex.py

import json
import os

API_FOLDER  = "api-catalogue"
OUTPUT_FILE = "apis_for_vertex.jsonl"  # 1 ligne JSON par API = format idéal pour Vertex AI

apis_converted = []
errors = []

files = [f for f in os.listdir(API_FOLDER) if f.endswith(".json")]
print(f"{len(files)} fichiers trouvés")

for filename in sorted(files):
    filepath = os.path.join(API_FOLDER, filename)
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = json.load(f)

        info = content.get("info", {})

        # Extrait les endpoints
        endpoints = []
        for path, methods in content.get("paths", {}).items():
            for method, details in methods.items():
                if method in ["get", "post", "put", "delete", "patch"]:
                    summary = details.get("summary", "")
                    if summary:
                        endpoints.append(f"{method.upper()} {path} — {summary}")

        # Format texte enrichi pour Vertex AI RAG
        api_name    = info.get("x-api-id", filename.replace(".json", ""))
        api_status  = info.get("x-status", "active")
        api_domain  = info.get("x-domain", "")
        api_version = info.get("x-api-version", "v1")
        api_team    = info.get("x-team", "")
        api_desc    = info.get("description", "")

        # Contenu textuel — Vertex AI va créer les embeddings depuis ce texte
        text_content = f"""API_NAME: {api_name}
API_TITLE: {info.get('title', '')}
API_VERSION: {api_version}
API_STATUS: {api_status}
API_DOMAIN: {api_domain}
API_TEAM: {api_team}
API_DESCRIPTION: {api_desc}
API_ENDPOINTS: {' | '.join(endpoints[:10])}
"""

        apis_converted.append({
            "id"      : api_name,
            "content" : text_content,
            "metadata": {
                "name"    : api_name,
                "status"  : api_status,
                "domain"  : api_domain,
                "version" : api_version,
                "team"    : api_team
            }
        })

    except Exception as e:
        errors.append({"file": filename, "error": str(e)})
        print(f"  ⚠ Erreur : {filename} → {e}")

# Sauvegarde en JSONL (1 ligne par API)
with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    for api in apis_converted:
        f.write(json.dumps(api, ensure_ascii=False) + "\n")

# Stats
size_kb = os.path.getsize(OUTPUT_FILE) / 1024
print(f"\n✅ {len(apis_converted)} APIs converties")
print(f"❌ {len(errors)} erreurs : {errors}")
print(f"📦 {OUTPUT_FILE} : {size_kb:.1f} KB")
print(f"\nExemple (1ère API) :")
print(apis_converted[0]["content"])