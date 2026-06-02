# Pricing API (pricing-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Prix dynamiques et promotions. Calcul des remises, codes promo et règles tarifaires. DIFFÉRENCE vs discount-api : Pricing calcule le prix final d'un produit en tenant compte de toutes les règles, Discount gère uniquement les campagnes de codes promo.

## Endpoints
- GET /v1/pricing/product/{productId} : Prix actuel d'un produit
- POST /v1/pricing/calculate : Calculer le prix total d'un panier avec remises
- POST /v1/pricing/promo/validate : Valider un code promo
- GET /v1/pricing/rules : Lister les règles tarifaires
- POST /v1/pricing/rules : Créer une règle tarifaire
- PUT /v1/pricing/rules/{id} : Mettre à jour une règle

Authentification : Clé API Kong Gateway