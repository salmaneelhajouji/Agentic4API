# Auto Insurance API (auto-insurance-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Assurance automobile. Contrats, bonus-malus et constat amiable.

## Endpoints
- GET /v1/auto-insurance/{vehicleId} : Assurance véhicule
- POST /v1/auto-insurance/{vehicleId} : Souscrire
- GET /v1/auto-insurance/{contractId}/bonus-malus : Coefficient B/M
- POST /v1/auto-insurance/accident-report : Créer constat amiable

Authentification : apiKey