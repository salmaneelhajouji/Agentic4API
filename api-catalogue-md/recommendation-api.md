# Recommendation API (recommendation-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Data

Recommandations personnalisées de produits. Collaboratif et basé sur le contenu.

## Endpoints
- GET /v1/recommendations/{userId} : Recommandations personnalisées pour un utilisateur
- GET /v1/recommendations/similar/{productId} : Produits similaires
- GET /v1/recommendations/trending : Produits tendance
- POST /v1/recommendations/feedback : Feedback sur une recommandation (clic, achat, rejet)

Authentification : Clé API Kong Gateway