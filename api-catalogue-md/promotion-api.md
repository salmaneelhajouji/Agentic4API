# Promotion API (promotion-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Marketing

Promotions commerciales automatiques. Remises sans code (ex: -20% sur toute la catégorie). DIFFÉRENCE vs discount-api : Promotion = remise automatique sans code (s'applique sur critères produits/segments), Discount = code promo saisi par l'utilisateur. DIFFÉRENCE vs pricing-api : Promotion crée les règles de remise, Pricing les applique au calcul final.

## Endpoints
- POST /v1/promotions : Créer une promotion automatique
- GET /v1/promotions : Lister les promotions actives et planifiées
- GET /v1/promotions/{id} : Détails d'une promotion
- PUT /v1/promotions/{id} : Modifier une promotion
- PUT /v1/promotions/{id}/activate : Activer
- PUT /v1/promotions/{id}/deactivate : Désactiver
- POST /v1/promotions/eligible : Promotions applicables à un panier donné

Authentification : Clé API Kong Gateway — contacter votre équipe platform