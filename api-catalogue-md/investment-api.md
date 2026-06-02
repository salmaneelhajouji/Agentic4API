# Investment API (investment-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Placements financiers OPCVM, ETF, obligations. Catalogue produits et passation ordres. DIFFERENCE vs portfolio-api : Investment = passation ordres et catalogue, Portfolio = analyse portefeuille existant.

## Endpoints
- GET /v1/investments/{clientId} : Portefeuille client
- GET /v1/investments/products : Catalogue produits
- GET /v1/investments/orders : Ordres en cours
- POST /v1/investments/orders : Passer ordre

Authentification : apiKey