"""verifier_coherence.py — version robuste (gere tous les formats de dataset)."""
import os, sys, json

def charger_dataset(chemin):
    with open(chemin, encoding='utf-8-sig') as f:   # utf-8-sig enleve le BOM
        contenu = f.read()
    # 1) tentative : c'est du JSON pur ?
    try:
        return json.loads(contenu)
    except Exception:
        pass
    # 2) tentative : c'est du Python (GOLDEN_DATASET = [...] ou autre) ?
    ns = {}
    try:
        exec(contenu, ns)
    except Exception as e:
        raise ValueError(f"Impossible de lire le fichier : {e}")
    # cherche GOLDEN_DATASET, sinon la 1ere liste de dicts trouvee
    if 'GOLDEN_DATASET' in ns and isinstance(ns['GOLDEN_DATASET'], list):
        return ns['GOLDEN_DATASET']
    for v in ns.values():
        if isinstance(v, list) and v and isinstance(v[0], dict):
            return v
    raise ValueError("Aucune liste de questions trouvee dans le fichier")

def main(md_dir, dataset_path):
    if not os.path.isdir(md_dir):
        print(f"ERREUR : dossier introuvable : {md_dir}"); return
    noms_md = {f[:-3] for f in os.listdir(md_dir) if f.endswith('.md')}
    print(f"Fichiers .md trouves      : {len(noms_md)}")

    dataset = charger_dataset(dataset_path)
    noms_dataset = set()
    for q in dataset:
        for api in q.get('expected_apis', []):
            noms_dataset.add(api)
    print(f"APIs attendues (dataset)  : {len(noms_dataset)}")
    print(f"Questions dans le dataset : {len(dataset)}")
    print("=" * 60)

    manquants = sorted(noms_dataset - noms_md)
    if manquants:
        print(f"\n[!] {len(manquants)} API(s) du dataset SANS fichier .md :")
        for n in manquants:
            print(f"      - {n}")
    else:
        print("\n[OK] Toutes les APIs du dataset ont un fichier .md correspondant.")

    jamais = sorted(noms_md - noms_dataset)
    print(f"\n[info] {len(jamais)} fichier(s) .md non references par le dataset (normal)")

    print("\n" + "=" * 60)
    if not manquants:
        print("VERDICT : catalogue Markdown ALIGNE avec le dataset. Pret a indexer.")
    else:
        print("VERDICT : corriger les noms manquants AVANT d'indexer.")

if __name__ == "__main__":
    md_dir       = sys.argv[1] if len(sys.argv) > 1 else "api-catalogue-md"
    dataset_path = sys.argv[2] if len(sys.argv) > 2 else "golden_dataset.py"
    main(md_dir, dataset_path)