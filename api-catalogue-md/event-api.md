# Event API (event-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Gestion des événements métier publiés sur le bus d'événements (Event Bus). Publication, souscription et replay. DIFFÉRENCE vs event-tracking-api : Event API est le bus d'événements système (ordre.créé, paiement.réussi) pour la communication entre microservices, Event Tracking API collecte les événements comportementaux utilisateurs pour l'analytics. DIFFÉRENCE vs calendar-api : Event API = événements systèmes asynchrones, Calendar API = événements humains planifiés dans le temps.

## Endpoints
- POST /v1/events/publish : Publier un événement sur le bus
- POST /v1/events/subscriptions : Souscrire à un type d'événement
- GET /v1/events/subscriptions : Lister les souscriptions actives
- GET /v1/events : Consulter le journal des événements passés
- POST /v1/events/replay : Rejouer des événements passés (utile après incident)
- GET /v1/events/types : Catalogue des types d'événements disponibles

Authentification : Clé API Kong Gateway — Devoteam nexDigital