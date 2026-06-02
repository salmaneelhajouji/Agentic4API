# Trading API (trading-api-v2)
Version v2 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Trading actions, obligations, derives. Ordres market/limit/stop. DIFFERENCE vs investment-api : Trading = execution temps reel marches, Investment = gestion epargne retail.

## Endpoints
- GET /v2/trading/orders : Carnet ordres
- POST /v2/trading/orders : Passer ordre
- GET /v2/trading/orders/{id} : Ordre
- DELETE /v2/trading/orders/{id} : Annuler
- GET /v2/trading/market-data : Cotations temps reel

Authentification : apiKey