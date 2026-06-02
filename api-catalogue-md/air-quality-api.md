# Air Quality API (air-quality-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Qualité de l'air intérieur et extérieur. CO2, PM2.5, COV et indices AQI.

## Endpoints
- GET /v1/air-quality/{sensorId} : Données qualité air
- POST /v1/air-quality/{sensorId} : Enregistrer
- GET /v1/air-quality/{sensorId}/history : Historique
- GET /v1/air-quality/alerts : Alertes
- POST /v1/air-quality/alerts : Créer alerte

Authentification : apiKey