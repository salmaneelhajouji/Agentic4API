# Medical Record API (medical-record-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Actes cliniques, diagnostics et historique médical. DIFFÉRENCE vs patient-api : Medical Record = actes médicaux (diagnostics, consultations), Patient API = identité administrative.

## Endpoints
- GET /v1/records/{patientId} : Historique actes
- POST /v1/records/{patientId} : Ajouter acte
- GET /v1/records/{patientId}/diagnoses : Diagnostics
- POST /v1/records/{patientId}/diagnoses : Poser diagnostic
- GET /v1/records/{patientId}/procedures : Actes
- POST /v1/records/{patientId}/procedures : Enregistrer

Authentification : apiKey