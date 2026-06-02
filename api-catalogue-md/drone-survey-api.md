# Drone Survey API (drone-survey-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Relevés par drone. Cartographie NDVI, détection stress et rapports.

## Endpoints
- GET /v1/drone-surveys : Relevés planifiés
- POST /v1/drone-surveys : Planifier relevé
- GET /v1/drone-surveys/{id} : Indice NDVI
- GET /v1/drone-surveys/{id}/anomalies : Anomalies cultures

Authentification : apiKey