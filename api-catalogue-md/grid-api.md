# Grid API (grid-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Gestion réseau électrique intelligent. Flux de puissance, équilibrage et incidents.

## Endpoints
- GET /v1/grid/status : Statut réseau
- GET /v1/grid/nodes : Noeuds du réseau
- POST /v1/grid/nodes : Ajouter noeud
- GET /v1/grid/nodes/{id} : Detail noeud
- PUT /v1/grid/nodes/{id} : Modifier
- GET /v1/grid/incidents : Incidents en cours
- POST /v1/grid/incidents : Signaler

Authentification : apiKey