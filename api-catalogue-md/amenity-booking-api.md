# Amenity Booking API (amenity-booking-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Réservation équipements partagés. Salles de réunion, parking, buanderie. DIFFERENCE vs meeting-room-api : Amenity Booking = équipements résidentiels, Meeting Room = salles de réunion professionnelles.

## Endpoints
- GET /v1/amenities : Equipements disponibles
- GET /v1/amenities/{id}/bookings : Réservations
- POST /v1/amenities/{id}/bookings : Réserver
- DELETE /v1/amenities/{id}/bookings/{bookingId} : Annuler

Authentification : apiKey