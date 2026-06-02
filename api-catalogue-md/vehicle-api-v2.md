# Vehicle API (vehicle-api-v2)
Version v2 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Données techniques véhicule. Diagnostics OBD, kilométrage et état. DIFFERENCE vs fleet-api : Vehicle = données techniques d'un seul véhicule, Fleet = gestion de l'ensemble de la flotte.

## Endpoints
- GET /v2/vehicles/{id} : Données véhicule
- PUT /v2/vehicles/{id} : Modifier
- GET /v2/vehicles/{id}/diagnostics : Diagnostics OBD
- POST /v2/vehicles/{id}/diagnostics : Lancer diagnostic
- GET /v2/vehicles/{id}/mileage : Kilométrage

Authentification : apiKey