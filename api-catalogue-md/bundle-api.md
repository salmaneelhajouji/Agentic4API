# Bundle API (bundle-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Packs et bundles de produits. Création, tarification et gestion des lots.

## Endpoints
- POST /v1/bundles : Créer un bundle produit
- GET /v1/bundles : Lister les bundles
- GET /v1/bundles/{id} : Détails d'un bundle
- PUT /v1/bundles/{id} : Modifier
- GET /v1/bundles/{id}/price : Prix calculé du bundle avec remise automatique

Authentification : apiKey