# Discount API (discount-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Marketing

Campagnes de remise et codes de réduction. Création, activation et suivi des promotions. DIFFÉRENCE vs pricing-api : Discount gère les campagnes et codes promo, Pricing calcule le prix final en intégrant toutes les règles dont les remises.

## Endpoints
- POST /v1/discounts : Créer un code de réduction
- GET /v1/discounts/{code} : Détails d'un code promo
- PUT /v1/discounts/{id}/activate : Activer un code promo
- PUT /v1/discounts/{id}/deactivate : Désactiver un code promo
- GET /v1/discounts/campaigns : Lister les campagnes promotionnelles

Authentification : Clé API Kong Gateway