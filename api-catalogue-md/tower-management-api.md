# Tower Management API (tower-management-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Antennes et pylones. Maintenance, partage et autorisations.

## Endpoints
- GET /v1/towers : Antennes
- POST /v1/towers : Enregistrer
- GET /v1/towers/{id} : Detail
- PUT /v1/towers/{id} : Modifier
- GET /v1/towers/{id}/maintenance : Maintenance
- POST /v1/towers/{id}/maintenance : Planifier
- GET /v1/towers/{id}/sharing : Accords partage

Authentification : apiKey