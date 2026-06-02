# Currency Exchange API (currency-exchange-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Change de devises. Taux temps réel, conversion et bureaux de change. DIFFERENCE vs interest-rate-api : Currency Exchange = taux change devises, Interest Rate = taux intérêt bancaires.

## Endpoints
- GET /v1/currency/rates : Taux de change
- POST /v1/currency/convert : Convertir montant
- GET /v1/currency/history/{pair} : Historique taux

Authentification : apiKey