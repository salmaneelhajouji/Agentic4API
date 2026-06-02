# Production Scheduling API (production-scheduling-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Ordonnancement production. Planning capacitaire, sequencement et optimisation.

## Endpoints
- GET /v1/scheduling/plan : Planning production
- POST /v1/scheduling/plan : Calculer ordonnancement
- GET /v1/scheduling/capacity : Charge capacitaire
- POST /v1/scheduling/capacity : Verifier capacite
- GET /v1/scheduling/jobs/{id} : Job ordonnance
- PUT /v1/scheduling/jobs/{id} : Reprogrammer

Authentification : apiKey