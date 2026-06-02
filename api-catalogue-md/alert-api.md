# Alert API (alert-api)
Version v1 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Alertes système et gestion des incidents. Pannes, seuils dépassés, escalades vers équipes OPS. DIFFÉRENCE vs notification-api : Alert cible les équipes techniques internes (PagerDuty, Slack ops), Notification cible les clients finaux. DIFFÉRENCE vs messaging-api : Alert est automatisé par des règles, Messaging est initié par un humain. DIFFÉRENCE vs email-api : Alert peut notifier par email mais son rôle est l'incident management.

## Endpoints
- POST /v1/alerts : Créer une alerte manuelle
- GET /v1/alerts : Lister les alertes actives
- PUT /v1/alerts/{id}/acknowledge : Acquitter une alerte
- PUT /v1/alerts/{id}/resolve : Résoudre une alerte
- GET /v1/alerts/rules : Lister les règles d'alerte
- POST /v1/alerts/rules : Créer une règle d'alerte automatique

Authentification : Clé API Kong Gateway