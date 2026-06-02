# Dispute Resolution API (dispute-resolution-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Resolution amiable des litiges. Mediation, arbitrage et conciliation.

## Endpoints
- GET /v1/disputes : Differends en cours
- POST /v1/disputes : Ouvrir differend
- GET /v1/disputes/{id} : Detail
- PUT /v1/disputes/{id} : Mettre a jour
- POST /v1/disputes/{id}/mediation : Clore sans accord

Authentification : apiKey