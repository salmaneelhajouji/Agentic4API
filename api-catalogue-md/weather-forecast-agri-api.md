# Weather Forecast Agri API (weather-forecast-agri-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Météo agricole hyperlocale. Prévisions, gelées et risques. DIFFERENCE vs energy-forecast-api : Weather Forecast Agri = météo parcelle agricole, Energy Forecast = prévisions consommation énergie.

## Endpoints
- GET /v1/weather/{fieldId} : Prévisions 10j
- GET /v1/weather/{fieldId}/frost-alerts : Alertes gelée
- GET /v1/weather/{fieldId}/agro-indices : Indices agrométéo

Authentification : apiKey