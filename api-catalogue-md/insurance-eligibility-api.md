# Insurance Eligibility API (insurance-eligibility-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Vérification droits assurance maladie AMO/AMC et calcul reste à charge. DIFFÉRENCE vs health-insurance-api : Insurance Eligibility = vérification droits côté soin, Health Insurance = gestion contrats côté assureur.

## Endpoints
- POST /v1/eligibility/check : Vérifier droits ouverts
- GET /v1/eligibility/{patientId} : Droits du patient
- GET /v1/eligibility/{patientId}/coverage : Détail couverture

Authentification : apiKey