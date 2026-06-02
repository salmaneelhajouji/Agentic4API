# Portfolio API (portfolio-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Gestion portefeuille actifs. Valorisation, performance et rebalancement. DIFFERENCE vs investment-api : Portfolio = analyse existant, Investment = passation ordres.

## Endpoints
- GET /v1/portfolios/{clientId} : Valorisation
- POST /v1/portfolios/{clientId} : Creer
- GET /v1/portfolios/{id}/performance : Performance TRI
- POST /v1/portfolios/{id}/rebalance : Reequilibrer

Authentification : apiKey