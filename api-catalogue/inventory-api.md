# Inventory API

## Description
API de gestion des stocks et inventaires produits. Suivi en temps réel des niveaux de stock, alertes de rupture et réapprovisionnement automatique.

## Team
Equipe Logistique

## Version
v3

## Endpoints
- GET /v3/inventory
- GET /v3/inventory/{productId}
- PUT /v3/inventory/{productId}/stock
- POST /v3/inventory/alerts
- POST /v3/inventory/restock
- DELETE /v3/inventory/{productId}