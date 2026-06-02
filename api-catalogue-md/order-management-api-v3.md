# Order Management API (order-management-api-v3)
Version v3 - statut : active
Domaine : Retail
Equipe : Equipe Retail

Gestion commandes omnicanal. Cycle de vie, fractionnement et retours. DIFFERENCE vs cart-api : Order Management = commande validée et en cours de traitement, Cart = panier en cours de constitution.

## Endpoints
- GET /v3/orders : Commandes
- POST /v3/orders : Créer commande
- GET /v3/orders/{id} : Detail
- PUT /v3/orders/{id} : Modifier
- DELETE /v3/orders/{id} : Annuler
- GET /v3/orders/{id}/status : Statut
- PUT /v3/orders/{id}/status : Changer statut
- GET /v3/orders/{id}/returns : Retours
- POST /v3/orders/{id}/returns : Initier retour

Authentification : apiKey