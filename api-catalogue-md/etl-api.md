# ETL API (etl-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Extract Transform Load. Jobs, transformations et chargement.

## Endpoints
- GET /v1/etl/jobs : Jobs
- POST /v1/etl/jobs : Creer
- GET /v1/etl/jobs/{id} : Detail
- PUT /v1/etl/jobs/{id} : Modifier
- POST /v1/etl/jobs/{id} : Executer
- GET /v1/etl/jobs/{id}/runs/{runId} : Logs

Authentification : apiKey