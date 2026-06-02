# Checkout API (checkout-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Tunnel d'achat et validation de commande. Orchestration du processus checkout : adresse, livraison, paiement. DIFFÉRENCE vs cart-api : Cart stocke les articles, Checkout orchestre les étapes de validation (adresse→livraison→paiement→confirmation). DIFFÉRENCE vs order-api : Checkout est le processus avant la commande, Order est le résultat après.

## Endpoints
- POST /v1/checkout/start : Démarrer une session checkout depuis le panier
- PUT /v1/checkout/{sessionId}/address : Étape 1 : Définir l'adresse de livraison
- GET /v1/checkout/{sessionId}/shipping : Étape 2 : Options de livraison disponibles
- PUT /v1/checkout/{sessionId}/shipping : Sélectionner une option de livraison
- PUT /v1/checkout/{sessionId}/payment : Étape 3 : Définir le moyen de paiement
- POST /v1/checkout/{sessionId}/confirm : Étape finale : Confirmer et créer la commande

Authentification : Clé API Kong Gateway — contacter votre équipe platform