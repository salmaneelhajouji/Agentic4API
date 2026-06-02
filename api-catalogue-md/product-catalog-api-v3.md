# Product Catalog API (product-catalog-api-v3)
Version v3 - statut : active
Domaine : Retail
Equipe : Equipe Retail

Catalogue produits omnicanal. Variantes, prix, medias et SEO. DIFFERENCE vs inventory-api : Product Catalog = fiche produit et description, Inventory = stock disponible.

## Endpoints
- GET /v3/products : Catalogue
- POST /v3/products : Créer produit
- GET /v3/products/{id} : Fiche produit
- PUT /v3/products/{id} : Modifier
- DELETE /v3/products/{id} : Supprimer
- GET /v3/products/{id}/variants : Variantes
- POST /v3/products/{id}/variants : Ajouter variante
- GET /v3/products/{id}/media : Medias
- POST /v3/products/{id}/media : Ajouter media
- GET /v3/products/search : Rechercher produits

Authentification : apiKey