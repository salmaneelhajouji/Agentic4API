# Price List API (price-list-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Listes de prix et catalogues tarifaires B2B. Prix négociés par client ou groupe. DIFFÉRENCE vs pricing-api : Price List = prix contractuels statiques par client/groupe (B2B), Pricing API = calcul dynamique temps réel avec règles promotionnelles.

## Endpoints
- POST /v1/price-lists : Créer une liste de prix
- GET /v1/price-lists : Lister les listes de prix
- GET /v1/price-lists/{id} : Détails d'une liste de prix
- PUT /v1/price-lists/{id} : Mettre à jour les prix
- POST /v1/price-lists/{id}/assign : Assigner une liste à un compte ou groupe
- POST /v1/price-lists/lookup : Prix effectif d'un produit pour un client donné

Authentification : Clé API Kong Gateway — contacter votre équipe platform