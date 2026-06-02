# Number Management API (number-management-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Gestion numeros. Attribution, portabilite et SDA.

## Endpoints
- GET /v1/numbers : Numeros
- POST /v1/numbers : Attribuer
- GET /v1/numbers/{number} : Info
- DELETE /v1/numbers/{number} : Liberer
- POST /v1/numbers/{number}/portability : Initier portabilite
- GET /v1/numbers/{number}/portability : Statut

Authentification : apiKey