# HVAC API (hvac-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Systèmes de chauffage, ventilation et climatisation. Contrôle température et qualité air.

## Endpoints
- GET /v1/hvac/{unitId} : Statut HVAC
- PUT /v1/hvac/{unitId} : Changer mode
- GET /v1/hvac/{unitId}/schedule : Planning
- PUT /v1/hvac/{unitId}/schedule : Modifier planning

Authentification : apiKey