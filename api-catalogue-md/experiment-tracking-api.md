# Experiment Tracking API (experiment-tracking-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Suivi experiences ML. Runs, metriques et comparaison.

## Endpoints
- GET /v1/experiments : Experiences
- POST /v1/experiments : Creer
- GET /v1/experiments/{id} : Detail
- PUT /v1/experiments/{id} : Modifier
- GET /v1/experiments/{id}/runs : Runs
- POST /v1/experiments/{id}/runs : Demarrer
- GET /v1/experiments/{id}/runs/{runId}/metrics : Metriques
- POST /v1/experiments/{id}/runs/{runId}/metrics : Logger

Authentification : apiKey