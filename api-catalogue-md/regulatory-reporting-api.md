# Regulatory Reporting API (regulatory-reporting-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Reporting reglementaire obligatoire. AMF, ACPR, DGFiP et soumissions automatisees.

## Endpoints
- GET /v1/regulatory/reports : Rapports reglementaires
- POST /v1/regulatory/reports : Créer rapport
- GET /v1/regulatory/reports/{id} : Statut soumission
- POST /v1/regulatory/reports/{id} : Soumettre au régulateur
- GET /v1/regulatory/deadlines : Échéances réglementaires

Authentification : apiKey