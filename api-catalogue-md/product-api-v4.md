# Product API (product-api-v4)
Version v4 - statut : active
Domaine : E-Commerce
Equipe : Equipe Catalog

Version actuelle et recommandée de l'API Produit. Introduit la gestion multi-catalogue (B2B/B2C), les bundles natifs, l'IA de description automatique et la conformité PIM complète. DIFFÉRENCE vs product-catalog-api : Product API gère le cycle de vie complet (création, variantes, SEO, publication), Product Catalog API gère la taxonomie et les catégories.

## Endpoints
- GET /v4/products : Lister produits multi-catalogue avec filtres IA
- POST /v4/products : Créer un produit avec description IA optionnelle
- GET /v4/products/{id} : Produit complet avec structured data JSON-LD
- PUT /v4/products/{id} : Mettre à jour
- DELETE /v4/products/{id} : Passer en end_of_life (jamais supprimé)
- GET /v4/products/{id}/variants : Variantes paginées (BREAKING: plus dans la réponse racine)
- POST /v4/products/{id}/variants : Ajouter une variante
- POST /v4/products/{id}/ai-description : Générer une description produit par IA (nouveau en v4)

Authentification : Clé API Kong Gateway — Devoteam nexDigital