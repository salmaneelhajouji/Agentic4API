# Data Versioning API (data-versioning-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Versioning datasets. Snapshots, diff et rollback.

## Endpoints
- GET /v1/versioning/{datasetId} : Versions
- POST /v1/versioning/{datasetId} : Creer snapshot
- GET /v1/versioning/{datasetId}/{version} : Detail version
- POST /v1/versioning/{datasetId}/{version} : Rollback

Authentification : apiKey