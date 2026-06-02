# Audit Log API (audit-log-api)
Version v1 - statut : active
Domaine : Security & Compliance
Equipe : Equipe Security

Journal d'audit et traçabilité. Toutes les actions sensibles enregistrées (qui a fait quoi, quand).

## Endpoints
- GET /v1/audit/logs : Consulter les logs d'audit
- POST /v1/audit/export : Exporter les logs en CSV pour audit externe

Authentification : Clé API Kong Gateway