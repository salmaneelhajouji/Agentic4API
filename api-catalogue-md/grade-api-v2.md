# Grade API (grade-api-v2)
Version v2 - statut : active
Domaine : Education
Equipe : Equipe Education

Notes et évaluations. Saisie, calcul moyennes et bulletins.

## Endpoints
- GET /v2/grades/{studentId} : Notes étudiant
- POST /v2/grades/{studentId} : Ajouter note
- GET /v2/grades/{studentId}/average : Moyenne générale
- GET /v2/grades/{studentId}/report-card : Bulletin de notes
- POST /v2/grades/{studentId}/report-card : Générer bulletin

Authentification : apiKey