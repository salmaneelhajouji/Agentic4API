# Battery Storage API (battery-storage-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Systèmes de stockage batterie. Etat de charge, cycles et gestion énergie.

## Endpoints
- GET /v1/batteries : Lister
- POST /v1/batteries : Enregistrer
- GET /v1/batteries/{id} : Etat batterie
- PUT /v1/batteries/{id} : Mode charge/décharge
- GET /v1/batteries/{id}/cycles : Historique cycles

Authentification : apiKey