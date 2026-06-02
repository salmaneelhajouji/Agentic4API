# Telemetry API (telemetry-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Données télémétrie équipements industriels. Agrégation, statistiques et anomalies. DIFFERENCE vs sensor-data-api : Telemetry = données agrégées équipements, Sensor Data = mesures brutes capteurs.

## Endpoints
- GET /v1/telemetry/{deviceId} : Données telemetrie
- POST /v1/telemetry/{deviceId} : Envoyer telemetrie
- GET /v1/telemetry/{deviceId}/stats : Statistiques
- GET /v1/telemetry/{deviceId}/anomalies : Detecter anomalies

Authentification : apiKey