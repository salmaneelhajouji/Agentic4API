# Power of Attorney API (power-of-attorney-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Procurations et mandats. Creation, validation et revocation.

## Endpoints
- GET /v1/poa : Procurations actives
- POST /v1/poa : Créer procuration
- GET /v1/poa/{id} : Detail procuration
- POST /v1/poa/{id} : Valider
- DELETE /v1/poa/{id} : Révoquer
- GET /v1/poa/{id}/scope : Périmètre delegation
- PUT /v1/poa/{id}/scope : Modifier périmètre

Authentification : apiKey