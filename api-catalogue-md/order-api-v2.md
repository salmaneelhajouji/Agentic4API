# Order API (order-api-v2)
Version v2 - statut : deprecated
Domaine : E-Commerce
Equipe : Equipe Commerce

Version 2 — DEPRECATED juin 2022. Introduit multi-articles, IDs préfixés ORD-, pagination et codes promo. Incompatible v1.

## Endpoints
- POST /v2/orders : Créer une commande multi-articles
- GET /v2/orders : Lister avec pagination
- GET /v2/orders/{id} : Récupérer une commande
- PUT /v2/orders/{id} : Modifier le statut
- PUT /v2/orders/{id}/cancel : Annuler une commande

Authentification : Clé API Kong Gateway