# extract_apis_guru_final.py
# Lance depuis : C:\Users\salmane.el.hajouji\Desktop\agentic4api\
# pip install pyyaml requests
#
# Cap = 3 SERVICES par domaine racine
# Ex: adyen.com → max 3 services (AccountService, CheckoutService, BinLookupService)
# Chaque service peut avoir 1 seule version (la preferred)
# Résultat : ~2000-2500 APIs, diversité maximale

import os, json, yaml, requests, time
from pathlib import Path
from collections import defaultdict

OUTPUT_DIR      = Path("apis_guru_json")
MAX_PER_DOMAIN  = 3      # max 3 services par domaine racine
TARGET_TOTAL    = 2500   # cap de sécurité
OUTPUT_DIR.mkdir(exist_ok=True)

# Récupérer la liste complète
print("📥 Récupération de la liste complète...")
response = requests.get(
    "https://api.apis.guru/v2/list.json",
    headers={"User-Agent": "Agentic4API-Research/1.0"},
    timeout=30
)
api_list = response.json()

total_providers = len(api_list)
total_specs     = sum(len(v.get("versions", {})) for v in api_list.values())
print(f"✅ {total_providers} providers · {total_specs} specs totales")
print(f"   Cap : {MAX_PER_DOMAIN} services/domaine · 1 version/service (preferred)")
print(f"   Cap de sécurité : {TARGET_TOTAL}\n")

# Compteur de services par domaine racine
# ex: domain_service_counts["adyen.com"] = {"AccountService", "CheckoutService"}
domain_service_counts = defaultdict(set)

ok, skipped, failed = 0, 0, []

for provider, provider_data in api_list.items():

    if ok >= TARGET_TOTAL:
        print(f"\n🎯 {TARGET_TOTAL} atteint — arrêt.")
        break

    # Extraire le domaine racine
    # "adyen.com/AccountService" → "adyen.com"
    # "stripe.com"               → "stripe.com"
    root_domain = provider.split("/")[0]

    # Extraire le nom du service
    # "adyen.com/AccountService" → "AccountService"
    # "stripe.com"               → "stripe.com" (pas de service séparé)
    service_name = provider.split("/")[1] if "/" in provider else provider

    # Skip si ce domaine a déjà MAX_PER_DOMAIN services différents
    if len(domain_service_counts[root_domain]) >= MAX_PER_DOMAIN:
        continue

    versions = provider_data.get("versions", {})
    if not versions:
        continue

    # Prendre UNIQUEMENT la version preferred
    # Si pas de preferred → prendre la dernière
    best_version = None
    best_data    = None

    for vk, vd in versions.items():
        if vd.get("info", {}).get("x-preferred", False):
            best_version = vk
            best_data    = vd
            break

    if not best_version:
        # Pas de preferred → dernière version
        best_version = list(versions.keys())[-1]
        best_data    = list(versions.values())[-1]

    spec_url = (best_data.get("swaggerUrl") or
                best_data.get("openapiUrl") or "")
    if not spec_url:
        skipped += 1
        continue

    # Nom du fichier
    safe     = lambda s: s.replace("/", "__").replace(":", "-").replace(" ", "-")
    filename = f"{safe(provider)}__{safe(best_version)}.json"
    filepath = OUTPUT_DIR / filename

    if filepath.exists():
        domain_service_counts[root_domain].add(service_name)
        skipped += 1
        continue

    try:
        r = requests.get(
            spec_url,
            headers={"User-Agent": "Agentic4API-Research/1.0"},
            timeout=20
        )
        if r.status_code != 200:
            failed.append(f"{provider}: HTTP {r.status_code}")
            continue

        try:
            spec_data = (yaml.safe_load(r.text)
                         if spec_url.endswith((".yaml", ".yml"))
                         else json.loads(r.text))
        except Exception:
            try:    spec_data = yaml.safe_load(r.text)
            except: failed.append(f"{provider}: parse error"); continue

        if not isinstance(spec_data, dict):
            skipped += 1
            continue

        # Enrichir avec métadonnées
        info          = spec_data.get("info", {})
        api_guru_info = best_data.get("info", {})

        info["x-provider"]    = provider
        info["x-version-key"] = best_version
        info["x-preferred"]   = True
        info["x-categories"]  = api_guru_info.get("x-apisguru-categories", [])

        if not info.get("x-api-id"):
            api_id           = f"{provider.replace('.','_').replace('/','_')}__{best_version.replace('.','_').replace('/','_')}"
            info["x-api-id"] = api_id[:80]

        spec_data["info"] = info

        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(spec_data, f, ensure_ascii=False, indent=2)

        ok += 1
        domain_service_counts[root_domain].add(service_name)

        if ok % 100 == 0:
            pct = ok / TARGET_TOTAL * 100
            print(f"  [{ok:4}/{TARGET_TOTAL}] {pct:4.0f}%  ✅  {filename[:65]}")

    except requests.exceptions.Timeout:
        failed.append(f"{provider}: timeout")
    except Exception as e:
        failed.append(f"{provider}: {str(e)[:60]}")

    time.sleep(0.15)

# ── Résultat final ───────────────────────────────────────────────────────
all_files = list(OUTPUT_DIR.glob("*.json"))
domains_done = len(domain_service_counts)

print(f"\n{'='*65}")
print(f"  ✅ Téléchargés         : {ok}")
print(f"  ⏭️  Skippés            : {skipped}")
print(f"  ❌ Échecs              : {len(failed)}")
print(f"  📁 Fichiers JSON       : {len(all_files)}")
print(f"  🌐 Domaines couverts   : {domains_done}")
print(f"{'='*65}")

# Top 15 domaines
print(f"\n  Top 15 domaines :")
sorted_domains = sorted(domain_service_counts.items(),
                        key=lambda x: -len(x[1]))
for domain, services in sorted_domains[:15]:
    bar = "█" * len(services)
    print(f"    {domain:<40} {len(services)}  {bar}")
    for s in sorted(services):
        print(f"      └─ {s}")

# Rapport
with open("extraction_report.json", "w") as f:
    json.dump({
        "ok": ok, "skipped": skipped,
        "total_files": len(all_files),
        "domains_covered": domains_done,
        "max_per_domain": MAX_PER_DOMAIN,
        "failed_count": len(failed),
        "failed_sample": failed[:20]
    }, f, indent=2)

print("\n✅ Rapport → extraction_report.json")
print("✅ Extraction terminée — prêt pour Pinecone")