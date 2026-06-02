# Demand Response API (demand-response-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Effacement et flexibilité énergétique. Programmes demand response et rémunération.

## Endpoints
- GET /v1/programs : Programmes DR disponibles
- POST /v1/programs : S'inscrire
- GET /v1/programs/{id}/events : Evénements en cours
- POST /v1/programs/{id}/events : Activer effacement
- GET /v1/programs/{id}/rewards : Récompenses accumulées

Authentification : apiKey