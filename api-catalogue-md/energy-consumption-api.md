# Energy Consumption API (energy-consumption-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Consommation énergétique bâtiments et installations. Courbes de charge et optimisation.

## Endpoints
- GET /v1/consumption/{siteId} : Consommation actuelle
- POST /v1/consumption/{siteId} : Enregistrer
- GET /v1/consumption/{siteId}/history : Historique
- GET /v1/consumption/{siteId}/forecast : Prévisions consommation

Authentification : apiKey