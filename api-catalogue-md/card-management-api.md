# Card Management API (card-management-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Cartes bancaires debit/credit. Activation, plafonds, opposition et cartes virtuelles.

## Endpoints
- GET /v1/cards/{clientId} : Cartes du client
- POST /v1/cards/{clientId} : Commander
- GET /v1/cards/{id} : Detail
- PUT /v1/cards/{id} : Modifier plafonds
- POST /v1/cards/{id}/block : Opposition
- DELETE /v1/cards/{id}/block : Lever opposition
- POST /v1/cards/{id}/virtual : Carte virtuelle

Authentification : apiKey