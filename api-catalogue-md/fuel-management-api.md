# Fuel Management API (fuel-management-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion carburant flotte. Consommation, ravitaillement et coûts.

## Endpoints
- GET /v1/fuel/{vehicleId} : Niveau carburant
- POST /v1/fuel/{vehicleId} : Enregistrer ravitaillement
- GET /v1/fuel/consumption/{fleetId} : Coûts carburant

Authentification : apiKey