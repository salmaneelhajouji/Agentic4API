# Log API (log-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Centralisation et consultation des logs applicatifs. Recherche, filtres et alertes sur patterns.

## Endpoints
- GET /v1/logs : Consulter les logs
- POST /v1/logs : Publier un log
- GET /v1/logs/tail/{service} : Logs en temps réel (Server-Sent Events)
- POST /v1/logs/patterns : Créer une alerte sur un pattern de log

Authentification : Clé API Kong Gateway — contacter votre équipe platform