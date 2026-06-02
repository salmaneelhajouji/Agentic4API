# Fraud Telecom API (fraud-telecom-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Fraude telecom. IRSF, SIM swap et appels frauduleux. DIFFERENCE vs fraud-detection-api : Fraud Telecom = usage telecom, Fraud Detection = transactions bancaires.

## Endpoints
- POST /v1/fraud-telecom/score : Scorer usage
- GET /v1/fraud-telecom/sim-swap : Alertes
- POST /v1/fraud-telecom/sim-swap : Bloquer
- GET /v1/fraud-telecom/alerts : Alertes
- PUT /v1/fraud-telecom/alerts : Resoudre

Authentification : apiKey