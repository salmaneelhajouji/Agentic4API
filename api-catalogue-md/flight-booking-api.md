# Flight Booking API (flight-booking-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Réservation vols. Recherche, sièges et check-in en ligne.

## Endpoints
- POST /v1/flights/search : Rechercher vols
- GET /v1/flights/{id} : Detail vol
- POST /v1/flights/{id} : Réserver vol
- GET /v1/flights/{bookingId}/seat : Plan cabine
- POST /v1/flights/{bookingId}/seat : Choisir siège
- POST /v1/flights/{bookingId}/checkin : Check-in en ligne
- POST /v1/flights/{bookingId}/cancel : Annuler vol

Authentification : apiKey