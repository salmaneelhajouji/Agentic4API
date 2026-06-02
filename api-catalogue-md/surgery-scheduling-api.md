# Surgery Scheduling API (surgery-scheduling-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Planification chirurgicale. Blocs opératoires, équipes chirurgicales et liste d'attente.

## Endpoints
- GET /v1/surgeries : Planning blocs
- POST /v1/surgeries : Planifier intervention
- GET /v1/surgeries/{id} : Détail
- PUT /v1/surgeries/{id} : Modifier
- DELETE /v1/surgeries/{id} : Annuler
- GET /v1/or/availability : Disponibilité blocs

Authentification : apiKey