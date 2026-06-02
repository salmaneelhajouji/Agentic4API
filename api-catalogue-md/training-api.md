# Training API (training-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Formation professionnelle. Catalogue, inscriptions et suivi des compétences.

## Endpoints
- GET /v1/trainings : Catalogue des formations
- POST /v1/trainings/{id}/enroll : S'inscrire à une formation
- GET /v1/trainings/{employeeId}/completed : Formations complétées par un employé
- GET /v1/skills/{employeeId} : Compétences validées d'un employé
- PUT /v1/skills/{employeeId} : Mettre à jour les compétences

Authentification : Clé API Kong Gateway