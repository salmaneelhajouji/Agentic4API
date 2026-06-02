# Patient Admission API (patient-admission-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Admission et sortie administrative. Check-in, attribution lit et facturation séjour. DIFFÉRENCE vs emergency-api : Admission = entrée planifiée, Emergency = urgences non planifiées.

## Endpoints
- GET /v1/admissions : Admissions en cours
- POST /v1/admissions : Admettre
- GET /v1/admissions/{id} : Dossier
- PUT /v1/admissions/{id} : Modifier
- POST /v1/admissions/{id}/discharge : Sortie administrative

Authentification : apiKey