# Event Tracking API (event-tracking-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Collecte d'événements comportementaux utilisateurs. Clics, pages vues, funnels de conversion.

## Endpoints
- POST /v1/events/track : Enregistrer un événement utilisateur
- POST /v1/events/batch : Envoi groupé d'événements
- GET /v1/events/funnels/{funnelId} : Analyse d'un funnel de conversion
- GET /v1/events/sessions/{userId} : Sessions d'un utilisateur

Authentification : Clé API Kong Gateway