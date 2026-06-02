# Data Usage API (data-usage-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Consommation data mobile. Quotas et throttling.

## Endpoints
- GET /v1/data-usage/{lineId} : Quota restant
- GET /v1/data-usage/{lineId}/history : Historique
- GET /v1/data-usage/{lineId}/throttling : Statut
- POST /v1/data-usage/{lineId}/throttling : Appliquer
- DELETE /v1/data-usage/{lineId}/throttling : Lever

Authentification : apiKey