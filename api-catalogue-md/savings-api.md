# Savings API (savings-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Comptes epargne (Livret A, LDDS, PEL). Taux, plafonds et versements programmes.

## Endpoints
- GET /v1/savings/{clientId} : Livrets du client
- POST /v1/savings/{clientId} : Ouvrir livret
- GET /v1/savings/{id} : Detail
- POST /v1/savings/{id} : Versement

Authentification : apiKey