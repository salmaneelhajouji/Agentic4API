# Tooling API (tooling-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Gestion outillage. Outils coupants, durees de vie et reconditionnement.

## Endpoints
- GET /v1/tooling : Outillage
- POST /v1/tooling : Ajouter outil
- GET /v1/tooling/{id} : Statut outil
- PUT /v1/tooling/{id} : Mettre a jour duree vie
- GET /v1/tooling/{id}/reconditioning : Reconditionnements
- POST /v1/tooling/{id}/reconditioning : Planifier

Authentification : apiKey