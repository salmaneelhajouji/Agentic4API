# Time Tracking API (time-tracking-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Suivi du temps de travail. Pointage, heures supplémentaires et rapports d'activité.

## Endpoints
- POST /v1/time/clock-in : Pointer l'arrivée
- POST /v1/time/clock-out : Pointer le départ
- GET /v1/time/{employeeId}/entries : Entrées de temps d'un employé
- GET /v1/time/{employeeId}/summary : Résumé heures/semaine/mois

Authentification : Clé API Kong Gateway — contacter votre équipe platform