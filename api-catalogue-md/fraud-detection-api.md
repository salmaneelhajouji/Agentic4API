# Fraud Detection API (fraud-detection-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Detection fraude temps reel sur transactions. DIFFERENCE vs fraud-claims-api assurance : Fraud Detection = transactions bancaires, Fraud Claims = sinistres assurance.

## Endpoints
- POST /v1/fraud/score : Scorer transaction
- GET /v1/fraud/rules : Regles actives
- POST /v1/fraud/rules : Ajouter regle
- GET /v1/fraud/alerts : Alertes fraude
- PUT /v1/fraud/alerts : Resoudre

Authentification : apiKey