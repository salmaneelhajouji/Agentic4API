# Attendance API (attendance-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Présences et absences. Suivi assiduité, justificatifs et alertes.

## Endpoints
- GET /v1/attendance/{studentId} : Présences
- POST /v1/attendance/{studentId} : Enregistrer
- GET /v1/attendance/{studentId}/absences : Absences
- POST /v1/attendance/{studentId}/absences : Justifier absence
- GET /v1/attendance/alerts : Alertes assiduité

Authentification : apiKey