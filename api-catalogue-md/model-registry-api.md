# Model Registry API (model-registry-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Registre modeles ML. Versions, metriques et deploiement.

## Endpoints
- GET /v1/models : Modeles
- POST /v1/models : Enregistrer
- GET /v1/models/{id} : Detail
- PUT /v1/models/{id} : Modifier
- GET /v1/models/{id}/versions : Versions
- POST /v1/models/{id}/versions : Ajouter
- POST /v1/models/{id}/versions/{version}/deploy : Deployer
- DELETE /v1/models/{id}/versions/{version}/deploy : Retirer

Authentification : apiKey