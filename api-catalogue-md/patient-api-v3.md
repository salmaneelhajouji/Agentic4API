# Patient API (patient-api-v3)
Version v3 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Dossier patient complet HL7 FHIR avec consentements RGPD et alertes médicales. DIFFÉRENCE vs medical-record-api : Patient API = identité et admission, Medical Record = actes cliniques.

## Endpoints
- GET /v3/patients : Lister avec filtres FHIR
- POST /v3/patients : Admettre patient
- GET /v3/patients/{id} : Dossier FHIR complet
- PUT /v3/patients/{id} : Modifier
- DELETE /v3/patients/{id} : Sortie patient
- GET /v3/patients/{id}/alerts : Alertes médicales
- POST /v3/patients/{id}/alerts : Créer alerte
- GET /v3/patients/{id}/consent : Consentements RGPD
- PUT /v3/patients/{id}/consent : Modifier

Authentification : apiKey