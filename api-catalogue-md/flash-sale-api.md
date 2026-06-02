# Flash Sale API (flash-sale-api)
Version v1 - statut : active
Domaine : Retail
Equipe : Equipe Retail

Ventes flash et offres limitees. Compteur, stock dedie et urgence.

## Endpoints
- GET /v1/flash-sales : Ventes flash actives
- POST /v1/flash-sales : Créer vente flash
- GET /v1/flash-sales/{id} : Detail
- PUT /v1/flash-sales/{id} : Modifier
- DELETE /v1/flash-sales/{id} : Terminer
- GET /v1/flash-sales/{id}/stock : Stock dedie
- POST /v1/flash-sales/{id}/stock : Réserver article

Authentification : apiKey