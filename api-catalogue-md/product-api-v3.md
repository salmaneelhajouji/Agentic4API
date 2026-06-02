# Product API (product-api-v3)
Version v3 - statut : active
Domaine : E-Commerce
Equipe : Equipe Catalog

Version actuelle. Produits enrichis avec SEO, variantes en sous-ressource, category_id lié au catalogue et currency obligatoire. Recommandée pour tous les nouveaux développements.

## Endpoints
- GET /v3/products : Lister les produits avec SEO et filtres enrichis
- POST /v3/products : Créer un produit complet
- GET /v3/products/{id} : Détails complets d'un produit
- PUT /v3/products/{id} : Mettre à jour
- DELETE /v3/products/{id} : Archiver le produit
- GET /v3/products/{id}/variants : Variantes d'un produit
- POST /v3/products/{id}/variants : Ajouter une variante
- PUT /v3/products/{id}/variants/{variantId} : Modifier une variante
- DELETE /v3/products/{id}/variants/{variantId} : Supprimer une variante

Authentification : Clé API Kong Gateway — contacter votre équipe platform