# Health Check API (health-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Monitoring de la santé des services. Status, disponibilité et métriques de performance.

## Endpoints
- GET /v1/health : Statut global de la plateforme
- GET /v1/health/services : Statut de chaque microservice
- GET /v1/health/dependencies : Dépendances externes (DB, cache, APIs)
- GET /v1/health/metrics : Métriques de performance en temps réel

Authentification : Clé API Kong Gateway