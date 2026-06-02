# Wishlist API (wishlist-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Listes de souhaits clients. Produits désirés sans intention d'achat immédiate, partage et notifications de disponibilité. DIFFÉRENCE vs cart-api : Wishlist = désirs futurs, Cart = intention d'achat immédiate.

## Endpoints
- GET /v1/wishlists/{userId} : Récupérer la wishlist
- POST /v1/wishlists/{userId}/items : Ajouter un produit
- DELETE /v1/wishlists/{userId}/items/{itemId} : Supprimer de la wishlist
- POST /v1/wishlists/{userId}/share : Partager la wishlist
- POST /v1/wishlists/{userId}/move-to-cart : Déplacer des articles vers le panier

Authentification : Clé API Kong Gateway