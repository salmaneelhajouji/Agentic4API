# Car Rental API (car-rental-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Location de voitures. Disponibilité, tarifs et contrats.

## Endpoints
- GET /v1/car-rental/vehicles : Véhicules disponibles
- GET /v1/car-rental/bookings : Réservations
- POST /v1/car-rental/bookings : Réserver véhicule
- GET /v1/car-rental/bookings/{id} : Detail
- PUT /v1/car-rental/bookings/{id} : Modifier
- DELETE /v1/car-rental/bookings/{id} : Annuler
- GET /v1/car-rental/bookings/{id}/contract : Contrat location

Authentification : apiKey