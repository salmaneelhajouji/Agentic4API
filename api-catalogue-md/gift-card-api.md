# Gift Card API (gift-card-api)
Version v1 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Cartes cadeaux et bons d'achat. Émission, activation, utilisation et suivi du solde.

## Endpoints
- POST /v1/gift-cards/issue : Émettre une carte cadeau
- GET /v1/gift-cards/{code} : Solde et validité d'une carte cadeau
- POST /v1/gift-cards/{code}/redeem : Utiliser une carte cadeau pour payer
- GET /v1/gift-cards/{code}/balance-history : Historique des utilisations

Authentification : apiKey