# Inventory Industry API (inventory-industry-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Stocks industriels. Matieres premieres, composants et produits finis. DIFFERENCE vs inventory-api : Inventory Industry = stocks de production, Inventory = stock retail.

## Endpoints
- GET /v1/stock : Articles en stock
- POST /v1/stock : Ajouter
- GET /v1/stock/{id} : Niveau stock
- POST /v1/stock/{id} : Ajuster stock
- GET /v1/stock/movements : Mouvements
- POST /v1/stock/movements : Enregistrer

Authentification : apiKey