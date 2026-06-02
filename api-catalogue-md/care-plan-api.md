# Care Plan API (care-plan-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Plans de soins personnalisés. Objectifs thérapeutiques, tâches et suivi observance.

## Endpoints
- GET /v1/care-plans/{patientId} : Plans actifs
- POST /v1/care-plans/{patientId} : Créer plan
- GET /v1/care-plans/{id}/tasks : Tâches du plan
- POST /v1/care-plans/{id}/tasks : Ajouter tâche
- PATCH /v1/care-plans/{id}/tasks : Statut tâche

Authentification : apiKey