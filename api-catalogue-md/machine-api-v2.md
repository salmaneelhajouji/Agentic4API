# Machine API (machine-api-v2)
Version v2 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Gestion machines industrielles. Etat, capacite et programmes CNC. DIFFERENCE vs device-registry-api : Machine = equipment industriel lourd avec programmes usinage, Device Registry = appareils IoT generiques.

## Endpoints
- GET /v2/machines : Machines
- POST /v2/machines : Ajouter
- GET /v2/machines/{id} : Detail
- PUT /v2/machines/{id} : Modifier
- GET /v2/machines/{id}/status : Etat machine
- PUT /v2/machines/{id}/status : Changer etat
- GET /v2/machines/{id}/programs : Programmes CNC
- POST /v2/machines/{id}/programs : Charger programme

Authentification : apiKey