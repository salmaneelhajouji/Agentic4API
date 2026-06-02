# Tutor API (tutor-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Tutorat et accompagnement. Mise en relation tuteurs/étudiants et sessions.

## Endpoints
- GET /v1/tutors : Tuteurs disponibles
- POST /v1/tutors : S'inscrire comme tuteur
- GET /v1/tutors/{id} : Disponibilités
- GET /v1/tutoring/sessions : Sessions
- POST /v1/tutoring/sessions : Réserver session
- GET /v1/tutoring/sessions/{id} : Detail
- DELETE /v1/tutoring/sessions/{id} : Annuler

Authentification : apiKey