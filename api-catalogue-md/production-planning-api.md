# Production Planning API (production-planning-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Planification production. PDP, MPS et gestion capacite.

## Endpoints
- GET /v1/planning/pdp : Plan directeur
- POST /v1/planning/pdp : Mettre a jour PDP
- GET /v1/planning/capacity/{workcenter} : Plan capacite
- POST /v1/planning/capacity/{workcenter} : Ajuster

Authentification : apiKey