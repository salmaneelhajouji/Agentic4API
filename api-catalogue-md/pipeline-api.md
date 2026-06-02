# Pipeline API (pipeline-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Pipelines de donnees. Orchestration, monitoring et alertes.

## Endpoints
- GET /v1/pipelines : Pipelines
- POST /v1/pipelines : Creer
- GET /v1/pipelines/{id} : Detail
- PUT /v1/pipelines/{id} : Modifier
- DELETE /v1/pipelines/{id} : Supprimer
- GET /v1/pipelines/{id}/runs : Executions
- POST /v1/pipelines/{id}/runs : Declencher
- GET /v1/pipelines/{id}/runs/{runId} : Statut
- DELETE /v1/pipelines/{id}/runs/{runId} : Annuler

Authentification : apiKey