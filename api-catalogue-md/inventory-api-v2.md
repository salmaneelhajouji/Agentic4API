# Inventory API (inventory-api-v2)
Version v2 - statut : deprecated
Domaine : Supply Chain
Equipe : Equipe Logistique

Version 2 inventaire — DEPRECATED depuis 2023, migrer vers v3. Introduit les alertes de seuil configurables, l'historique des mouvements et le support multi-entrepôt basique. Incompatible avec v1 (IDs entiers → string ITEM-XXX).

## Endpoints
- GET /v2/inventory : Inventaire global avec filtres entrepôt
- GET /v2/inventory/{itemId} : Stock d'un produit
- PUT /v2/inventory/{itemId} : Mettre à jour le stock (BREAKING v3: remplacé par PATCH /stock)
- GET /v2/inventory/{itemId}/movements : Historique des mouvements de stock (nouveau en v2)
- POST /v2/inventory/alerts : Configurer alerte de seuil bas (nouveau en v2)
- GET /v2/inventory/alerts : Lister les alertes configurées

Authentification : Clé API Kong Gateway — Devoteam nexDigital