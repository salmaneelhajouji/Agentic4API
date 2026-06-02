# Warehouse API (warehouse-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Entrepôts et emplacements physiques. Mouvements de stock inter-entrepôts. DIFFÉRENCE vs inventory-api : Warehouse = où sont les produits (entrepôt, allée, étagère), Inventory = combien en stock.

## Endpoints
- GET /v1/warehouses : Lister les entrepôts
- GET /v1/warehouses/{id}/stock : Stock d'un entrepôt
- POST /v1/warehouses/transfer : Transférer du stock entre entrepôts
- GET /v1/warehouses/{id}/locations : Emplacements dans un entrepôt (allées, étagères)

Authentification : Clé API Kong Gateway