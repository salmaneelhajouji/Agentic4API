# Calendar API (calendar-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Gestion des calendriers et disponibilités internes. Plannings des conseillers, techniciens et ressources. DIFFÉRENCE vs appointment-api : Calendar = gestion des disponibilités et plannings côté équipes, Appointment = réservation côté client.

## Endpoints
- GET /v1/calendars/{resourceId} : Calendrier d'une ressource
- GET /v1/calendars/{resourceId}/availability : Disponibilités d'une ressource sur une période
- POST /v1/calendars/{resourceId}/events : Ajouter un événement au calendrier

Authentification : Clé API Kong Gateway — contacter votre équipe platform