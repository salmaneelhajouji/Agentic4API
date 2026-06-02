# Energy Forecast API (energy-forecast-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Prévisions consommation énergétique. Modèles ML et courbes de charge. DIFFERENCE vs energy-consumption-api : Forecast = prévisions futures, Consumption = données historiques.

## Endpoints
- GET /v1/forecast/{siteId} : Prévisions 24h/7j
- POST /v1/forecast/{siteId} : Calculer prévision
- GET /v1/forecast/{siteId}/accuracy : Précision modèle

Authentification : apiKey