# Configuration API (configuration-api)
Version v1 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Gestion configuration applicative. Parametres, secrets et environnements.

## Endpoints
- GET /v1/config/{appId} : Config application
- PUT /v1/config/{appId} : Mettre a jour
- GET /v1/config/{appId}/{env} : Config par env
- PUT /v1/config/{appId}/{env} : Definir config
- GET /v1/config/{appId}/secrets : Secrets
- POST /v1/config/{appId}/secrets : Definir secret
- DELETE /v1/config/{appId}/secrets : Supprimer

Authentification : apiKey