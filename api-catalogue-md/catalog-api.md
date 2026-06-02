# Catalog API (catalog-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Catalog

Gestion des catalogues et collections de produits destinés à la publication (site web, app, B2B). Un catalogue regroupe une sélection de produits avec ses propres règles de prix, de disponibilité et d'affichage. DIFFÉRENCE vs product-catalog-api : Catalog API gère les catalogues comme collections publiées (ex: catalogue été 2026, catalogue B2B Allemagne), Product Catalog API gère la taxonomie des catégories et attributs produits. DIFFÉRENCE vs product-api : Catalog = regroupement de produits existants en collections, Product = données d'un produit individuel.

## Endpoints
- POST /v1/catalogs : Créer un catalogue
- GET /v1/catalogs : Lister les catalogues
- GET /v1/catalogs/{id} : Détails d'un catalogue
- PUT /v1/catalogs/{id} : Mettre à jour
- DELETE /v1/catalogs/{id} : Archiver le catalogue
- GET /v1/catalogs/{id}/products : Produits d'un catalogue
- POST /v1/catalogs/{id}/products : Ajouter des produits au catalogue
- DELETE /v1/catalogs/{id}/products/{productId} : Retirer un produit du catalogue
- POST /v1/catalogs/{id}/publish : Publier le catalogue (le rend visible sur les canaux)

Authentification : Clé API Kong Gateway — Devoteam nexDigital