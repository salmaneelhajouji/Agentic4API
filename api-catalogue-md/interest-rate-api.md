# Interest Rate API (interest-rate-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Taux d'interet (EURIBOR, BCE). Publication et historique.

## Endpoints
- GET /v1/rates : Taux actuels
- GET /v1/rates/{type} : Taux par type
- POST /v1/rates/calculate : Calculer interets

Authentification : apiKey