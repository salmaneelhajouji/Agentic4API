# E-Discovery API (e-discovery-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Decouverte electronique. Collecte, preservation et analyse documents pour litiges.

## Endpoints
- GET /v1/ediscovery/holds : Holds actifs
- POST /v1/ediscovery/holds : Creer hold
- GET /v1/ediscovery/holds/{id} : Detail
- POST /v1/ediscovery/holds/{id} : Lever hold
- GET /v1/ediscovery/collections/{id} : Collection
- POST /v1/ediscovery/collections/{id} : Exporter

Authentification : apiKey