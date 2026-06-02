# Feature Store API (feature-store-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Registre features ML. Creation, versioning et serving.

## Endpoints
- GET /v1/features : Features
- POST /v1/features : Creer
- GET /v1/features/{id} : Detail
- PUT /v1/features/{id} : Modifier
- GET /v1/features/{id}/versions : Versions
- POST /v1/features/{id}/versions : Publier
- POST /v1/features/serving : Features offline

Authentification : apiKey