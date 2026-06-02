# Rate Limiting API (rate-limiting-api)
Version v1 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Gestion quotas et rate limiting. Par client, endpoint et periode.

## Endpoints
- GET /v1/rate-limits : Quotas configures
- POST /v1/rate-limits : Creer quota
- GET /v1/rate-limits/{id} : Detail
- PUT /v1/rate-limits/{id} : Modifier
- POST /v1/rate-limits/check : Consommer quota

Authentification : apiKey