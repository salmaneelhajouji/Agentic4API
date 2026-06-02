# Data Catalog API (data-catalog-api-v3)
Version v3 - statut : active
Domaine : Data
Equipe : Equipe Data

Catalogue donnees central. Metadonnees, lineage, qualite et gouvernance. DIFFERENCE vs metadata-api : Data Catalog = gouvernance enterprise, Metadata = metadonnees fichiers.

## Endpoints
- GET /v3/datasets : Catalogue
- POST /v3/datasets : Enregistrer
- GET /v3/datasets/{id} : Detail
- PUT /v3/datasets/{id} : Modifier
- DELETE /v3/datasets/{id} : Deprecer
- GET /v3/datasets/{id}/lineage : Lineage complet
- GET /v3/datasets/{id}/quality : Score qualite
- POST /v3/datasets/{id}/quality : Lancer controle
- GET /v3/datasets/{id}/glossary : Termes metier
- POST /v3/datasets/{id}/glossary : Ajouter terme

Authentification : apiKey