# Health Monitoring API (health-monitoring-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Monitoring continu patients hospitalisés. Agrégation capteurs IoT médicaux et alertes temps réel.

## Endpoints
- GET /v1/monitoring/{patientId} : Données monitoring
- POST /v1/monitoring/{patientId} : Configurer
- GET /v1/monitoring/alerts : Alertes actives
- PUT /v1/monitoring/alerts : Acquitter

Authentification : apiKey