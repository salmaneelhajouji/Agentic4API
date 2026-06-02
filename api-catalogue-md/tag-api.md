# Tag API (tag-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Tags libres et labels sur les ressources (produits, tickets, contrats, clients). Taxonomie folksonomy. DIFFÉRENCE vs segmentation-api : Tag = étiquette libre assignée manuellement à une ressource spécifique, Segmentation = groupe dynamique calculé selon des règles comportementales sur des populations d'utilisateurs. DIFFÉRENCE vs product-catalog-api : Tag = label libre multi-domaine, Category = hiérarchie structurée propre au catalogue produit.

## Endpoints
- GET /v1/tags : Lister tous les tags disponibles
- POST /v1/tags : Créer un tag
- PUT /v1/tags/{id} : Mettre à jour un tag
- DELETE /v1/tags/{id} : Supprimer un tag (dé-tagge toutes les ressources associées)
- POST /v1/tags/assign : Assigner des tags à une ressource
- GET /v1/tags/resources : Ressources portant un ou plusieurs tags

Authentification : Clé API Kong Gateway — Devoteam nexDigital