# Contract Analytics API (contract-analytics-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Analyse contrats par IA. Extraction clauses, risques et comparaison. DIFFERENCE vs contract-api : Contract Analytics = analyse IA existants, Contract = gestion cycle de vie.

## Endpoints
- POST /v1/contract-analytics/{contractId} : Analyser contrat
- GET /v1/contract-analytics/{contractId} : Risques identifies
- POST /v1/contract-analytics/compare : Comparer contrats

Authentification : apiKey