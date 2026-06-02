# CDR API (cdr-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Detail communications CDR. DIFFERENCE vs billing-telecom-api : CDR = enregistrements bruts, Billing Telecom = factures.

## Endpoints
- GET /v1/cdr/calls : CDR appels
- POST /v1/cdr/calls : Exporter
- GET /v1/cdr/sms : CDR SMS
- GET /v1/cdr/data : CDR data

Authentification : apiKey