# Packaging API (packaging-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Gestion emballages. References, conditionnements et gestion retours.

## Endpoints
- GET /v1/packaging : Types emballage
- POST /v1/packaging : Ajouter
- POST /v1/packaging/{orderId}/pack : Conditionner ordre
- GET /v1/packaging/{orderId}/pack : Liste colisage
- GET /v1/packaging/returns : Retours emballages
- POST /v1/packaging/returns : Traiter retour

Authentification : apiKey