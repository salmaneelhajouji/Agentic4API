# Cart API (cart-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Gestion du panier d'achat temporaire. Ajout, modification, suppression d'articles avant commande. Gère les sessions anonymes. DIFFÉRENCE vs order-api : Cart = panier temporaire avant achat, Order = commande confirmée après achat. DIFFÉRENCE vs wishlist-api : Cart = intention d'achat immédiate, Wishlist = désirs futurs sans intention immédiate.

## Endpoints
- GET /v1/cart/{userId} : Récupérer le panier d'un utilisateur
- POST /v1/cart/{userId}/items : Ajouter un article au panier
- PUT /v1/cart/{userId}/items/{itemId} : Modifier la quantité d'un article
- DELETE /v1/cart/{userId}/items/{itemId} : Supprimer un article du panier
- POST /v1/cart/{userId}/checkout : Valider le panier et créer une commande
- DELETE /v1/cart/{userId}/clear : Vider le panier

Authentification : Clé API Kong Gateway