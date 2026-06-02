# Dispatch API (dispatch-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Dispatch et affectation missions. Optimisation affectations conducteurs/véhicules/missions.

## Endpoints
- GET /v1/missions : Missions disponibles
- POST /v1/missions : Créer mission
- GET /v1/missions/{id} : Detail
- PUT /v1/missions/{id} : Modifier
- POST /v1/missions/{id}/assign : Affecter conducteur
- DELETE /v1/missions/{id}/assign : Désaffecter
- POST /v1/dispatch/optimize : Optimiser affectations

Authentification : apiKey