# Product Catalog API (product-catalog-api)
Version v2 - statut : active
Domaine : E-Commerce
Equipe : Equipe Catalog

Catalogue produits. CRUD complet sur produits, catégories et attributs. DIFFÉRENCE vs search-api : Catalog = gestion des données produits, Search = interrogation du catalogue.

## Endpoints
- GET /v2/products : Lister les produits
- POST /v2/products : Créer un produit
- GET /v2/products/{id} : Détails d'un produit
- PUT /v2/products/{id} : Mettre à jour un produit
- DELETE /v2/products/{id} : Archiver un produit
- GET /v2/categories : Lister les catégories
- POST /v2/categories : Créer une catégorie

Authentification : Clé API Kong Gateway