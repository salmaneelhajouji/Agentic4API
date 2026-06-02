# Network API (network-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Gestion reseau telecom. Noeuds, couverture et qualite de service.

## Endpoints
- GET /v1/network/nodes : Noeuds
- POST /v1/network/nodes : Ajouter
- GET /v1/network/coverage/{location} : Couverture
- GET /v1/network/qos : Metriques QoS
- GET /v1/network/incidents : Incidents
- POST /v1/network/incidents : Signaler

Authentification : apiKey