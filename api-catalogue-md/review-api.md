# Review API (review-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Catalog

Avis textuels et notations produits. Soumission, modération et agrégation des reviews clients. DIFFÉRENCE vs rating-api : Review contient le texte complet et la note, Rating gère uniquement la note numérique sans texte.

## Endpoints
- POST /v1/reviews : Soumettre un avis produit
- GET /v1/reviews/product/{productId} : Avis d'un produit
- DELETE /v1/reviews/product/{productId} : Supprimer tous les avis d'un produit (admin)
- PUT /v1/reviews/{id}/moderate : Modérer un avis (approuver/rejeter)
- DELETE /v1/reviews/{id} : Supprimer un avis
- GET /v1/reviews/stats/{productId} : Statistiques des avis d'un produit

Authentification : Clé API Kong Gateway