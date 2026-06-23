import os
import json
from pathlib import Path

def fusionner_catalogue_api(dossier_source, fichier_sortie):
    """
    Lit tous les fichiers .json d'un dossier et les rassemble 
    dans un seul et unique fichier JSON.
    """
    catalogue_combine = []
    path_dossier = Path(dossier_source)
    
    # Étape 1 : Récupérer tous les fichiers .json du dossier
    fichiers_json = list(path_dossier.glob("*.json"))
    print(f"🔍 {len(fichiers_json)} fichiers JSON détectés dans '{dossier_source}'.")
    
    # Étape 2 : Lecture et agrégation
    for chemin_fichier in fichiers_json:
        try:
            with open(chemin_fichier, 'r', encoding='utf-8') as f:
                contenu = json.load(f)
                
                # Optionnel : Conserver une trace du nom de fichier d'origine si besoin
                # contenu['info']['x-source-file'] = chemin_fichier.name
                
                catalogue_combine.append(contenu)
                
        except json.JSONDecodeError:
            print(f"❌ Erreur : '{chemin_fichier.name}' n'est pas un JSON valide et a été ignoré.")
        except Exception as e:
            print(f"⚠️ Erreur inattendue sur '{chemin_fichier.name}' : {e}")
            
    # Étape 3 : Écriture du fichier unique consolidé
    try:
        with open(fichier_sortie, 'w', encoding='utf-8') as f_out:
            json.dump(catalogue_combine, f_out, ensure_ascii=False, indent=2)
        print(f"✅ Fusion réussie ! {len(catalogue_combine)} APIs regroupées dans '{fichier_sortie}'.")
    except Exception as e:
        print(f"❌ Impossible d'écrire le fichier de sortie : {e}")

if __name__ == "__main__":
    # ⚙️ CONFIGURATION : Ajuste les chemins selon ton arborescence locale
    DOSSIER_APIS = "api-catalogue-v2.2.1" 
    FICHIER_UNIQUE = "api_catalogue_complet.json"
    
    fusionner_catalogue_api(DOSSIER_APIS, FICHIER_UNIQUE)