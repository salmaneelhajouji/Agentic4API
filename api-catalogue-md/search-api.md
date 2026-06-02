# Search API (search-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Platform

Recherche full-text sur le catalogue produits et commandes. Filtres, facettes et tri par pertinence. DIFFÉRENCE vs product-catalog-api : Search interroge les données, Product Catalog les gère.

## Endpoints
- GET /v1/search : Recherche globale
- GET /v1/search/products : Recherche produits avec facettes
- POST /v1/search/advanced : Recherche avancée avec filtres complexes
- GET /v1/search/suggestions : Autocomplétion et suggestions

Authentification : Clé API Kong Gateway