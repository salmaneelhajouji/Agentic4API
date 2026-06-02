# Assessment API (assessment-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Évaluations et examens. QCM, devoirs et corrections automatiques.

## Endpoints
- GET /v1/assessments : Évaluations
- POST /v1/assessments : Créer évaluation
- GET /v1/assessments/{id} : Detail
- PUT /v1/assessments/{id} : Modifier
- GET /v1/assessments/{id}/submissions : Rendus
- POST /v1/assessments/{id}/submissions : Corriger

Authentification : apiKey