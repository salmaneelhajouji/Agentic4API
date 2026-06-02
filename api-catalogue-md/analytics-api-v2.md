# Analytics API (analytics-api-v2)
Version v2 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Version 2 Analytics. Entonnoirs configurables, segments en temps réel, export streaming et dashboards partagés. DIFFÉRENCE vs v1 : ajout du streaming, des entonnoirs custom et du partage de dashboards.

## Endpoints
- GET /v2/analytics/sales : Métriques ventes v2
- POST /v2/analytics/funnels : Créer et analyser un entonnoir custom
- POST /v2/analytics/dashboard/share : Partager un dashboard avec un token d'accès public
- GET /v2/analytics/stream : Métriques temps réel en streaming (Server-Sent Events)

Authentification : apiKey