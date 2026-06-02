# Virtual Classroom API (virtual-classroom-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Classes virtuelles. Salles de cours en ligne, partage écran et enregistrement.

## Endpoints
- GET /v1/classrooms : Classes planifiées
- POST /v1/classrooms : Créer classe
- GET /v1/classrooms/{id} : Detail
- POST /v1/classrooms/{id} : Démarrer cours
- DELETE /v1/classrooms/{id} : Terminer cours
- GET /v1/classrooms/{id}/participants : Participants
- POST /v1/classrooms/{id}/participants : Inviter
- GET /v1/classrooms/{id}/recording : Enregistrement

Authentification : apiKey