# Concierge API (concierge-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Services conciergerie hôtelière. Réservations, recommandations et assistance.

## Endpoints
- GET /v1/concierge/{hotelId} : Services disponibles
- GET /v1/concierge/{hotelId}/requests : Demandes en cours
- POST /v1/concierge/{hotelId}/requests : Créer demande
- GET /v1/concierge/{hotelId}/recommendations : Recommandations locales

Authentification : apiKey