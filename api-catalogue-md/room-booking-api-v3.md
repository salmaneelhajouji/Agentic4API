# Room Booking API (room-booking-api-v3)
Version v3 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Réservation chambres avec garanties et politiques annulation. DIFFERENCE vs amenity-booking-api : Room Booking = chambre d'hôtel, Amenity Booking = équipements résidentiels partagés.

## Endpoints
- GET /v3/bookings : Réservations
- POST /v3/bookings : Réserver chambre
- GET /v3/bookings/{id} : Detail réservation
- PUT /v3/bookings/{id} : Modifier
- DELETE /v3/bookings/{id} : Annuler
- POST /v3/bookings/{id}/payment : Rembourser
- POST /v3/bookings/check-availability : Vérifier disponibilité

Authentification : apiKey