# Metrics API (metrics-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Métriques techniques et business. KPIs d'ingénierie (latence, taux d'erreur) et business. DIFFÉRENCE vs analytics-api : Metrics = orienté ingénierie et monitoring, Analytics = orienté business et ventes.

## Endpoints
- POST /v1/metrics : Publier une métrique custom
- GET /v1/metrics/{name} : Récupérer une métrique sur une période
- GET /v1/metrics/kpis : KPIs techniques globaux
- POST /v1/metrics/query : Requête avancée multi-métriques

Authentification : Clé API Kong Gateway