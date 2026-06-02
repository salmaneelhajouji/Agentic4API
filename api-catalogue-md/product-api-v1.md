# Product API (product-api-v1)
Version v1 - statut : deprecated
Domaine : E-Commerce
Equipe : Equipe Catalog

Version initiale de l'API produits. DEPRECATED depuis 2022. ID entier, pas de variantes, images comme string simple. Migrer vers v2.

## Endpoints
- GET /v1/products : Lister les produits
- POST /v1/products : Créer un produit
- GET /v1/products/{id} : Récupérer un produit
- PUT /v1/products/{id} : Mettre à jour
- DELETE /v1/products/{id} : Supprimer définitivement (BREAKING v2: devient archive)

Authentification : Clé API Kong Gateway — contacter votre équipe platform