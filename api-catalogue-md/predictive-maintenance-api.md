# Predictive Maintenance API (predictive-maintenance-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Maintenance prédictive ML sur équipements industriels. Détection pannes anticipées et recommandations.

## Endpoints
- GET /v1/maintenance/predictions/{deviceId} : Prédictions pannes
- POST /v1/maintenance/predictions/{deviceId} : Lancer analyse
- GET /v1/maintenance/alerts : Alertes maintenance
- PUT /v1/maintenance/alerts : Acquitter
- GET /v1/maintenance/history/{deviceId} : Historique interventions

Authentification : apiKey