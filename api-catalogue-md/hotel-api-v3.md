# Hotel API (hotel-api-v3)
Version v3 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Gestion hotels complète. Chambres, tarifs dynamiques, services et avis. DIFFERENCE vs co-living-api : Hotel = hébergement touristique court séjour, Co-living = résidence longue durée.

## Endpoints
- GET /v3/hotels : Catalogue hotels
- POST /v3/hotels : Référencer hotel
- GET /v3/hotels/{id} : Fiche complete
- PUT /v3/hotels/{id} : Modifier
- GET /v3/hotels/{id}/rooms : Chambres disponibles
- POST /v3/hotels/{id}/rooms : Ajouter chambre
- GET /v3/hotels/{id}/rates : Tarifs dynamiques
- PUT /v3/hotels/{id}/rates : Mettre a jour
- GET /v3/hotels/{id}/reviews : Avis clients

Authentification : apiKey