# Scholarship API (scholarship-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Bourses et aides financières. Candidatures, critères et versements.

## Endpoints
- GET /v1/scholarships : Bourses disponibles
- POST /v1/scholarships : Candidater
- GET /v1/scholarships/{id} : Detail
- PUT /v1/scholarships/{id} : Instruire dossier
- GET /v1/scholarships/student/{studentId} : Bourses étudiant

Authentification : apiKey