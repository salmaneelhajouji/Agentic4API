# Recruitment API (recruitment-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Recrutement et candidatures. Offres d'emploi, candidats et processus de sélection.

## Endpoints
- POST /v1/jobs : Publier une offre d'emploi
- GET /v1/jobs : Lister les offres d'emploi
- POST /v1/jobs/{id}/apply : Postuler à une offre
- GET /v1/jobs/{id}/candidates : Candidats pour une offre
- PUT /v1/candidates/{id}/status : Mettre à jour le statut d'un candidat

Authentification : Clé API Kong Gateway