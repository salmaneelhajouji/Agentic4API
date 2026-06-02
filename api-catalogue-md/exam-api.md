# Exam API (exam-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Examens officiels. Planification, surveillance et résultats.

## Endpoints
- GET /v1/exams : Examens planifiés
- POST /v1/exams : Créer examen
- GET /v1/exams/{id} : Detail
- PUT /v1/exams/{id} : Modifier
- GET /v1/exams/{id}/candidates : Candidats inscrits
- POST /v1/exams/{id}/candidates : Inscrire candidat
- GET /v1/exams/{id}/results : Résultats
- POST /v1/exams/{id}/results : Publier

Authentification : apiKey