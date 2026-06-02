# Underwriting API (underwriting-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Souscription et acceptation du risque. Évaluation, décision et conditions.

## Endpoints
- POST /v1/underwriting/evaluate : Évaluer risque
- GET /v1/underwriting/{applicationId} : Décision souscription
- PUT /v1/underwriting/{applicationId} : Modifier decision
- GET /v1/underwriting/rules : Règles acceptation
- POST /v1/underwriting/rules : Ajouter règle

Authentification : apiKey