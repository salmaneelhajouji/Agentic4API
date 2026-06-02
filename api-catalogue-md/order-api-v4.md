# Order API (order-api-v4)
Version v4 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Version actuelle et recommandée. Gestion complète du cycle de vie des commandes e-commerce. Multi-articles, multi-devises, webhooks automatiques, expédition partielle. Utiliser cette version pour tous les nouveaux développements.

## Endpoints
- POST /v4/orders : Créer une commande complète
- GET /v4/orders : Lister avec filtres complets et tri
- GET /v4/orders/{id} : Récupérer une commande avec détails complets
- PUT /v4/orders/{id} : Modifier une commande (avant confirmation uniquement)
- DELETE /v4/orders/{id} : Supprimer (statut cancelled uniquement)
- PUT /v4/orders/{id}/cancel : Annuler et rembourser
- PATCH /v4/orders/{id}/status : Mettre à jour le statut (expédition, livraison) — webhook déclenché automatiquement
- POST /v4/orders/{id}/refund : Rembourser une commande livrée (total ou partiel)

Authentification : Clé API Kong Gateway