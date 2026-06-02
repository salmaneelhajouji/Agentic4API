# Excess API (excess-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Franchises et auto-rétentions. Calcul et application lors des sinistres.

## Endpoints
- GET /v1/excess/{contractId} : Montant franchise
- POST /v1/excess/{contractId} : Calculer franchise applicable
- GET /v1/excess/types : Types de franchises

Authentification : apiKey