# Risk Scoring API (risk-scoring-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Scoring risque assurance. Modèles actuariels et ML. DIFFERENCE vs credit-scoring-api : Risk Scoring = risque assurable (santé, auto, habitation), Credit Scoring = risque crédit bancaire.

## Endpoints
- POST /v1/risk/score : Calculer score risque
- GET /v1/risk/{clientId} : Score risque client
- GET /v1/risk/models : Modèles disponibles

Authentification : apiKey