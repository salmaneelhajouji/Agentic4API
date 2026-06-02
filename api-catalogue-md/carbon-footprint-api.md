# Carbon Footprint API (carbon-footprint-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Empreinte carbone installations et activités. Calcul CO2, reporting ESG et recommandations.

## Endpoints
- GET /v1/carbon/{siteId} : Empreinte carbone
- POST /v1/carbon/{siteId} : Calculer
- GET /v1/carbon/{siteId}/report : Rapport ESG
- POST /v1/carbon/{siteId}/report : Générer rapport
- GET /v1/carbon/offsets : Compensations carbone

Authentification : apiKey