# POS API (pos-api)
Version v1 - statut : active
Domaine : Retail
Equipe : Equipe Retail

Point of Sale en magasin. Transactions, tiroir-caisse et reçus.

## Endpoints
- GET /v1/pos/transactions : Transactions
- POST /v1/pos/transactions : Créer vente
- GET /v1/pos/transactions/{id} : Detail
- POST /v1/pos/transactions/{id} : Annuler vente
- GET /v1/pos/sessions : Session ouverte
- POST /v1/pos/sessions : Fermer caisse

Authentification : apiKey