# Rating API (rating-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Catalog

Notations numériques produits (1-5 étoiles). Scores moyens et distributions. DIFFÉRENCE vs review-api : Rating = note numérique seule, Review = texte complet + note. Cas d'usage : vote rapide sans rédiger un avis.

## Endpoints
- POST /v1/ratings : Soumettre une note
- GET /v1/ratings/product/{productId} : Toutes les notes d'un produit
- GET /v1/ratings/average/{productId} : Moyenne des notes
- GET /v1/ratings/distribution/{productId} : Distribution des notes (1 à 5 étoiles)

Authentification : Clé API Kong Gateway