# Farm Equipment API (farm-equipment-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Gestion matériel agricole. Tracteurs, machines et maintenance.

## Endpoints
- GET /v1/equipment : Matériel agricole
- POST /v1/equipment : Enregistrer matériel
- GET /v1/equipment/{id} : Detail
- PUT /v1/equipment/{id} : Modifier
- GET /v1/equipment/{id}/maintenance : Maintenance
- POST /v1/equipment/{id}/maintenance : Planifier entretien
- GET /v1/equipment/{id}/usage : Utilisation

Authentification : apiKey