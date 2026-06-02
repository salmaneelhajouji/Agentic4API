# Product API (product-api-v2)
Version v2 - statut : deprecated
Domaine : E-Commerce
Equipe : Equipe Catalog

Version 2 — DEPRECATED jan 2024. Introduit IDs préfixés PROD-, images multiples, variantes produit (taille/couleur) et structure pricing. Migrer vers v3.

## Endpoints
- GET /v2/products : Lister avec variantes
- POST /v2/products : Créer un produit avec variantes
- GET /v2/products/{id} : Détails d'un produit
- PUT /v2/products/{id} : Mettre à jour
- DELETE /v2/products/{id} : Archiver (soft delete)

Authentification : Clé API Kong Gateway — contacter votre équipe platform