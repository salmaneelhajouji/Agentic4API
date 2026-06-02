# Trip API (trip-api-v2)
Version v2 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion trajets et missions. Planification, suivi temps réel et bilan. DIFFERENCE vs route-optimization-api : Trip = trajet effectué, Route = calcul optimal d'itinéraire.

## Endpoints
- GET /v2/trips : Lister trajets
- POST /v2/trips : Créer trajet
- GET /v2/trips/{id} : Detail trajet
- PUT /v2/trips/{id} : Modifier
- POST /v2/trips/{id} : Terminer
- GET /v2/trips/{id}/waypoints : Points de passage
- POST /v2/trips/{id}/waypoints : Ajouter point

Authentification : apiKey