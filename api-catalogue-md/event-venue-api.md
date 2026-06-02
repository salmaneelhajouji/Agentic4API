# Event Venue API (event-venue-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Salles événementielles et lieux réception. Capacité, équipements et tarification. DIFFERENCE vs virtual-classroom-api : Event Venue = lieu physique événementiel, Virtual Classroom = salle de cours en ligne.

## Endpoints
- GET /v1/venues : Lieux disponibles
- POST /v1/venues : Référencer lieu
- GET /v1/venues/{id} : Disponibilité
- GET /v1/venues/{id}/bookings : Réservations
- POST /v1/venues/{id}/bookings : Réserver lieu

Authentification : apiKey