# Inventory API (inventory-api)
Version v3 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Stocks et inventaires produits en temps réel. Alertes rupture et réapprovisionnement automatique. DIFFÉRENCE vs warehouse-api : Inventory = quantités (combien ?), Warehouse = emplacements physiques (où ?).

## Endpoints
- GET /v3/inventory : Inventaire global
- DELETE /v3/inventory/{productId} : Archiver un produit de l'inventaire
- PUT /v3/inventory/{productId}/stock : Mettre à jour le stock
- POST /v3/inventory/alerts : Configurer une alerte de rupture
- POST /v3/inventory/restock : Déclencher un réapprovisionnement

Authentification : Clé API Kong Gateway