# Leave API (leave-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Congés et absences. Demandes, validations, soldes et calendrier.

## Endpoints
- POST /v1/leaves/request : Faire une demande de congé
- GET /v1/leaves/{employeeId} : Congés d'un employé
- PUT /v1/leaves/{id}/approve : Approuver une demande de congé
- PUT /v1/leaves/{id}/reject : Rejeter une demande de congé
- GET /v1/leaves/{employeeId}/balance : Solde de congés par type

Authentification : Clé API Kong Gateway