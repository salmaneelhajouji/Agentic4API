# Inventory API (inventory-api-v1)
Version v1 - statut : deprecated
Domaine : Supply Chain
Equipe : Equipe Logistique

Version 1 inventaire. DEPRECATED 2021. Pas d'alertes de seuil, pas de réapprovisionnement automatique, pas d'historique mouvements. Migrer vers v3.

## Endpoints
- GET /v1/inventory : Inventaire global
- GET /v1/inventory/{productId} : Stock d'un produit
- PUT /v1/inventory/{productId} : Mettre à jour le stock

Authentification : apiKey