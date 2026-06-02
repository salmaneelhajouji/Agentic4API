# Fleet API (fleet-api-v4)
Version v4 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion flotte complète. GPS, maintenance, consommation et conducteurs. DIFFERENCE vs vehicle-api : Fleet = gestion ensemble de la flotte, Vehicle = donnees d'un vehicule individuel.

## Endpoints
- GET /v4/vehicles : Lister flotte
- POST /v4/vehicles : Ajouter vehicule
- GET /v4/vehicles/{id} : Detail
- PUT /v4/vehicles/{id} : Modifier
- DELETE /v4/vehicles/{id} : Retirer
- GET /v4/vehicles/{id}/location : Position GPS temps reel
- GET /v4/vehicles/{id}/maintenance : Historique maintenance
- POST /v4/vehicles/{id}/maintenance : Planifier
- GET /v4/vehicles/{id}/fuel : Consommation

Authentification : apiKey