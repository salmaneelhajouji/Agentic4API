# Order API (order-api-v1)
Version v1 - statut : deprecated
Domaine : E-Commerce
Equipe : Equipe Commerce

Version initiale de l'API commandes. DEPRECATED depuis 2021. Ne supporte qu'un seul produit par commande, IDs entiers, pas de remises ni de pagination. Migrer vers v2.

## Endpoints
- POST /v1/orders : Créer une commande (mono-produit)
- GET /v1/orders : Lister les commandes
- GET /v1/orders/{id} : Récupérer une commande
- DELETE /v1/orders/{id} : Supprimer une commande — BREAKING: remplacé par /cancel en v2

Authentification : Clé API Kong Gateway