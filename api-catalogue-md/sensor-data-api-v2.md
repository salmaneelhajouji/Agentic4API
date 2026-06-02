# Sensor Data API (sensor-data-api-v2)
Version v2 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Collecte et analyse données capteurs IoT. Températures, pression, humidité et vibrations. DIFFERENCE vs telemetry-api : Sensor Data = données brutes capteurs physiques, Telemetry = données agrégées équipements.

## Endpoints
- GET /v2/sensors : Lister capteurs
- POST /v2/sensors : Enregistrer capteur
- GET /v2/sensors/{id} : Detail
- PUT /v2/sensors/{id} : Modifier
- GET /v2/sensors/{id}/data : Données temps reel
- POST /v2/sensors/{id}/data : Ingérer mesure
- GET /v2/sensors/{id}/stream : Stream SSE temps reel

Authentification : apiKey