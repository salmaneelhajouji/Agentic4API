# Metadata API (metadata-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Metadonnees techniques fichiers et objets. Schemas, tags et descriptions. DIFFERENCE vs data-catalog-api : Metadata = metadonnees techniques fichiers, Data Catalog = gouvernance enterprise.

## Endpoints
- GET /v1/metadata/{resourceId} : Metadonnees
- PUT /v1/metadata/{resourceId} : Mettre a jour
- POST /v1/metadata/{resourceId} : Ajouter tag

Authentification : apiKey