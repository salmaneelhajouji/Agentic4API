# Network Quality API (network-quality-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Qualite reseau et SLA. DIFFERENCE vs network-api : Network Quality = metriques QoS/SLA, Network = infrastructure noeuds.

## Endpoints
- GET /v1/network-quality/{siteId} : Qualite
- POST /v1/network-quality/{siteId} : Tester
- GET /v1/network-quality/sla : Violations

Authentification : apiKey