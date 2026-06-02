"""
convert_openapi_to_md_files.py  (v3 - identifiant = nom de fichier)
Convertit chaque OpenAPI JSON en fichier Markdown individuel.

LOGIQUE D'IDENTIFIANT :
Le nom du fichier source est la source de verite de l'identifiant.
  ab-testing-api.json  -> identifiant 'ab-testing-api'   (1 version)
  order-api-v4.json    -> identifiant 'order-api-v4'     (versionnee)
C'est ce qui correspond aux expected_apis du Golden Dataset.
On N'AJOUTE PAS de -v1 si le nom de fichier n'en a pas.

Usage :
    py convert_openapi_to_md_files.py ./api-catalogue ./api-catalogue-md
"""
import json, sys, glob, os

def openapi_to_markdown(spec, api_id):
    """spec OpenAPI + identifiant (= nom de fichier) -> texte markdown."""
    info = spec.get('info', {}) or {}
    title   = info.get('title', api_id)
    version = info.get('x-api-version', info.get('version', ''))
    status  = info.get('x-status', '')
    domain  = info.get('x-domain', '')
    team    = info.get('x-team', '')
    desc    = info.get('description', '')
    lines = [f"# {title} ({api_id})"]
    if version or status: lines.append(f"Version {version} - statut : {status}")
    if domain: lines.append(f"Domaine : {domain}")
    if team:   lines.append(f"Equipe : {team}")
    if desc:   lines.append(f"\n{desc}")
    eps = []
    for path, methods in (spec.get('paths', {}) or {}).items():
        if not isinstance(methods, dict): continue
        for m, det in methods.items():
            if m.lower() in ('get','post','put','patch','delete'):
                summary = (det.get('summary','') or det.get('operationId','')) if isinstance(det,dict) else ''
                eps.append(f"- {m.upper()} {path} : {summary}")
    if eps:
        lines.append("\n## Endpoints"); lines.extend(eps)
    sec = spec.get('components', {}).get('securitySchemes', {}) or {}
    for _, s in sec.items():
        if isinstance(s, dict):
            d = s.get('description') or s.get('type', '')
            if d: lines.append(f"\nAuthentification : {d}")
            break
    return "\n".join(lines)

def convert_folder(input_dir, output_dir):
    fichiers = sorted(glob.glob(os.path.join(input_dir, "**", "*.json"), recursive=True))
    if not fichiers:
        print(f"Aucun fichier .json trouve dans : {input_dir}"); return
    os.makedirs(output_dir, exist_ok=True)
    ok, erreurs, vus = 0, [], set()
    for fp in fichiers:
        # L'IDENTIFIANT = le nom du fichier sans extension (source de verite)
        api_id = os.path.splitext(os.path.basename(fp))[0]
        try:
            spec = json.load(open(fp, encoding='utf-8'))
            md = openapi_to_markdown(spec, api_id)
            out_name = f"{api_id}.md"
            if out_name in vus:
                erreurs.append((os.path.basename(fp), f"nom .md duplique : {out_name}"))
            vus.add(out_name)
            open(os.path.join(output_dir, out_name), 'w', encoding='utf-8').write(md)
            ok += 1
        except json.JSONDecodeError as e:
            erreurs.append((os.path.basename(fp), f"JSON invalide : {e}"))
        except Exception as e:
            erreurs.append((os.path.basename(fp), str(e)))
    print(f"OK : {ok} fichiers .md crees dans : {output_dir}/")
    print(f"   Fichiers JSON lus : {len(fichiers)}")
    if erreurs:
        print(f"\n{len(erreurs)} fichier(s) en erreur :")
        for nom, msg in erreurs[:20]:
            print(f"   - {nom} : {msg}")
    else:
        print("   Aucune erreur.")

if __name__ == "__main__":
    input_dir  = sys.argv[1] if len(sys.argv) > 1 else "api-catalogue"
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "api-catalogue-md"
    convert_folder(input_dir, output_dir)