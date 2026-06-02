# Tour Operator API (tour-operator-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Gestion tours et excursions. Guides, groupes et itinéraires.

## Endpoints
- GET /v1/tours : Tours disponibles
- POST /v1/tours : Créer tour
- GET /v1/tours/{id} : Detail tour
- PUT /v1/tours/{id} : Modifier
- GET /v1/tours/{id}/bookings : Réservations
- POST /v1/tours/{id}/bookings : Réserver place
- GET /v1/tours/{id}/guides : Guides assignés
- POST /v1/tours/{id}/guides : Assigner guide

Authentification : apiKey