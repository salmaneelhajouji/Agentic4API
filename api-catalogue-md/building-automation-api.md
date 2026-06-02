# Building Automation API (building-automation-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Automatisation bâtiments intelligents. HVAC, éclairage, sécurité et accès.

## Endpoints
- GET /v1/buildings/{id} : Statut bâtiment
- PUT /v1/buildings/{id} : Mode eco/confort
- GET /v1/buildings/{id}/zones : Zones du bâtiment
- POST /v1/buildings/{id}/zones : Ajouter zone
- GET /v1/buildings/{id}/energy : Consommation
- GET /v1/buildings/{id}/alerts : Alertes

Authentification : apiKey