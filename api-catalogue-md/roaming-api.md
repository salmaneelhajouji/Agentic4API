# Roaming API (roaming-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Roaming international. Accords, tarifs et consommation.

## Endpoints
- GET /v1/roaming/{subscriberId} : Statut
- POST /v1/roaming/{subscriberId} : Activer
- DELETE /v1/roaming/{subscriberId} : Desactiver
- GET /v1/roaming/{subscriberId}/usage : Consommation
- GET /v1/roaming/agreements : Accords
- POST /v1/roaming/agreements : Ajouter

Authentification : apiKey