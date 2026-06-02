# Health Check API (health-check-api)
Version v1 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Supervision etat des services. Ping, liveness, readiness et dependances.

## Endpoints
- GET /v1/health : Etat global
- GET /v1/health/services : Etat services
- POST /v1/health/services : Enregistrer service
- GET /v1/health/services/{id} : Detail service
- POST /v1/health/services/{id} : Lancer verification

Authentification : apiKey