# Toll API (toll-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion des péages et taxes de transit. Calcul coûts, télépéage et facturation.

## Endpoints
- POST /v1/tolls/calculate : Calculer péages itinéraire
- GET /v1/tolls/accounts/{vehicleId} : Compte télépéage
- POST /v1/tolls/accounts/{vehicleId} : Recharger compte
- GET /v1/tolls/transactions/{vehicleId} : Historique péages

Authentification : apiKey