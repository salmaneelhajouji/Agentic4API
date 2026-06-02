# Asset Tracking API (asset-tracking-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Suivi des actifs physiques en temps réel. GPS, géofencing et historique. DIFFERENCE vs logistics-tracking-api : Asset Tracking = actifs stationnaires (machines, équipements), Logistics = colis en transit.

## Endpoints
- GET /v1/assets : Lister actifs
- POST /v1/assets : Enregistrer
- GET /v1/assets/{id} : Position GPS
- PUT /v1/assets/{id} : Modifier
- GET /v1/assets/{id}/history : Historique positions
- POST /v1/assets/{id}/geofence : Créer zone
- GET /v1/assets/{id}/geofence : Vérifier zone

Authentification : apiKey