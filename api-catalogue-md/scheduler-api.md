# Scheduler API (scheduler-api)
Version v1 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Planification taches. CRON, one-shot et gestion erreurs.

## Endpoints
- GET /v1/scheduler/jobs : Jobs planifies
- POST /v1/scheduler/jobs : Planifier job
- GET /v1/scheduler/jobs/{id} : Detail
- PUT /v1/scheduler/jobs/{id} : Modifier
- DELETE /v1/scheduler/jobs/{id} : Supprimer
- POST /v1/scheduler/jobs/{id} : Executer maintenant
- GET /v1/scheduler/jobs/{id}/history : Historique executions

Authentification : apiKey