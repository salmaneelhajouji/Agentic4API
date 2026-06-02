# AML API (aml-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Anti-Money Laundering. Surveillance transactions blanchiment et financement terrorisme. DIFFERENCE vs kyc-api : AML = monitoring continu, KYC = verification identite initiale.

## Endpoints
- POST /v1/aml/monitor : Analyser transaction
- GET /v1/aml/alerts : Alertes AML
- PUT /v1/aml/alerts : Ouvrir investigation
- POST /v1/aml/reports : Declaration TRACFIN
- GET /v1/aml/reports : Historique

Authentification : apiKey