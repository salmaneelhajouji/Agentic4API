# Co-living API (co-living-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Gestion espaces co-living. Chambres, espaces partagés et services. DIFFERENCE vs hotel-api : Co-living = résidence longue durée avec espaces partagés, Hotel = hébergement touristique court séjour.

## Endpoints
- GET /v1/coliving/spaces : Espaces co-living
- POST /v1/coliving/spaces : Créer espace
- GET /v1/coliving/spaces/{id}/rooms : Chambres disponibles
- POST /v1/coliving/spaces/{id}/rooms : Réserver chambre
- GET /v1/coliving/spaces/{id}/amenities : Services

Authentification : apiKey