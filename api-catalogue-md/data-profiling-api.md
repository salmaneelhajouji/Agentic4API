# Data Profiling API (data-profiling-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Profilage donnees. Statistiques, distributions et patterns.

## Endpoints
- POST /v1/profiling/{datasetId} : Lancer profilage
- GET /v1/profiling/{datasetId} : Resultats
- GET /v1/profiling/{datasetId}/statistics : Taux nullite

Authentification : apiKey