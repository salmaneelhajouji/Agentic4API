# Claims Settlement API (claims-settlement-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Règlement sinistres et indemnisation. Calcul, paiement et quittance.

## Endpoints
- GET /v1/settlements : Règlements en cours
- POST /v1/settlements : Initier règlement
- GET /v1/settlements/{id} : Detail règlement
- POST /v1/settlements/{id} : Payer indemnité
- GET /v1/settlements/{id}/receipt : Quittance

Authentification : apiKey