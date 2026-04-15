# Inventory API

## Description
API de gestion des stocks et inventaires produits. Suivi en temps réel des niveaux de stock, alertes de rupture et réapprovisionnement automatique.

## Team
Equipe Logistique

## Version
v2

## Endpoints
- GET /v2/inventory
- GET /v2/inventory/{productId}
- PUT /v2/inventory/{productId}/stock
- POST /v2/inventory/alerts
- POST /v2/inventory/restock