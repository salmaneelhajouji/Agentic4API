# Pre-Order API (pre-order-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Pré-commandes pour produits non encore disponibles. Réservation, paiement différé et notifications de disponibilité.

## Endpoints
- POST /v1/pre-orders : Créer une pré-commande
- GET /v1/pre-orders/{id} : Statut d'une pré-commande
- DELETE /v1/pre-orders/{id} : Annuler une pré-commande
- POST /v1/pre-orders/product/{productId}/availability : Notifier les clients en pré-commande que le produit est disponible

Authentification : apiKey