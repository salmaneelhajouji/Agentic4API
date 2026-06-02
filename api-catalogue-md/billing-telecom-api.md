# Billing Telecom API (billing-telecom-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Facturation telecom. Factures, CDR et impayes. DIFFERENCE vs billing-api : Billing Telecom = usage telecom CDR/roaming, Billing = services generiques.

## Endpoints
- GET /v1/billing-telecom/{subscriberId} : Historique
- GET /v1/billing-telecom/{subscriberId}/cdr : Detail communications
- POST /v1/billing-telecom/{subscriberId}/disputes : Contester

Authentification : apiKey