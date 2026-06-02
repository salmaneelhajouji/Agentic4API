# Service Assurance API (service-assurance-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Assurance service telecom. SLA, incidents et resolution.

## Endpoints
- GET /v1/assurance/sla : Conformite SLA
- POST /v1/assurance/sla : Ouvrir violation
- GET /v1/assurance/incidents : Incidents
- POST /v1/assurance/incidents : Creer
- GET /v1/assurance/incidents/{id} : Detail
- POST /v1/assurance/incidents/{id} : Resoudre

Authentification : apiKey