# Credit Scoring API (credit-scoring-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Scoring credit et risque defaut. Modeles ML et notation Banque de France.

## Endpoints
- GET /v1/scoring/{clientId} : Score credit
- POST /v1/scoring/{clientId} : Demander score
- POST /v1/scoring/batch : Scoring en masse

Authentification : apiKey