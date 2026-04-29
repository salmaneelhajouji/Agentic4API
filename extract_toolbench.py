import zipfile
import os

ZIP_FILE   = "data.zip"
OUTPUT_DIR = "toolbench_data"

if not os.path.exists(ZIP_FILE):
    print("Erreur : data.zip introuvable dans le dossier courant.")
    print("Dossier actuel : " + os.getcwd())
    exit(1)

os.makedirs(OUTPUT_DIR, exist_ok=True)
print("ZIP trouve : " + ZIP_FILE)
print("Dossier de sortie : " + OUTPUT_DIR)
print()

print("Scan du ZIP...")
with zipfile.ZipFile(ZIP_FILE, 'r') as z:
    all_files = z.namelist()

print("Total fichiers dans le ZIP : " + str(len(all_files)))

tools_files = [
    f for f in all_files
    if 'toolenv/tools' in f
    and f.endswith('.json')
    and '__MACOSX' not in f
]

golden_files = [
    f for f in all_files
    if 'test_instruction' in f
    and f.endswith('.json')
    and '__MACOSX' not in f
]

useful = tools_files + golden_files

print("APIs tools     : " + str(len(tools_files)))
print("Golden dataset : " + str(len(golden_files)))
print("Total utiles   : " + str(len(useful)))
print()
print("Extraction de " + str(len(useful)) + " fichiers...")
print()

ok     = 0
errors = []

with zipfile.ZipFile(ZIP_FILE, 'r') as z:
    for i, member in enumerate(useful):
        try:
            z.extract(member, OUTPUT_DIR)
            ok += 1
            if ok % 500 == 0:
                pct = round(ok / len(useful) * 100, 1)
                print("  [" + str(ok) + "/" + str(len(useful)) + "] " + str(pct) + "%  " + member[:60])
        except Exception as e:
            errors.append(member + " : " + str(e))

print()
print("=" * 60)
print("EXTRACTION TERMINEE")
print("=" * 60)
print("Fichiers extraits : " + str(ok))
print("Erreurs           : " + str(len(errors)))
print()

tools_dir  = os.path.join(OUTPUT_DIR, "data", "toolenv", "tools")
golden_dir = os.path.join(OUTPUT_DIR, "data", "test_instruction")

if os.path.exists(tools_dir):
    categories = [d for d in os.listdir(tools_dir)
                  if os.path.isdir(os.path.join(tools_dir, d))]
    total_apis = 0
    for cat in categories:
        n = len([f for f in os.listdir(os.path.join(tools_dir, cat))
                 if f.endswith('.json')])
        total_apis += n

    print("Categories : " + str(len(categories)))
    print("Total APIs : " + str(total_apis))
    print()
    for cat in sorted(categories):
        n = len([f for f in os.listdir(os.path.join(tools_dir, cat))
                 if f.endswith('.json')])
        print("  " + cat.ljust(35) + " : " + str(n) + " APIs")

print()

if os.path.exists(golden_dir):
    golden = [f for f in os.listdir(golden_dir) if f.endswith('.json')]
    print("Golden dataset (" + str(len(golden)) + " fichiers) :")
    for f in sorted(golden):
        print("  " + f)

print()
print("=" * 60)
print("Pret pour l indexation dans Pinecone !")
print("=" * 60)