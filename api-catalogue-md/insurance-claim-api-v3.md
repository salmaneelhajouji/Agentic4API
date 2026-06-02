# Insurance Claim API (insurance-claim-api-v3)
Version v3 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Déclaration sinistres complète. Photo, expertise IA et suivi indemnisation. DIFFERENCE vs fraud-claims-api : Claim = sinistre légitime à indemniser, Fraud Claims = sinistre suspect à investiguer.

## Endpoints
- GET /v3/claims : Sinistres en cours
- POST /v3/claims : Déclarer sinistre
- GET /v3/claims/{id} : Detail
- PUT /v3/claims/{id} : Modifier
- POST /v3/claims/{id}/documents : Photos/docs
- GET /v3/claims/{id}/documents : Documents
- GET /v3/claims/{id}/assessment : Expertise
- POST /v3/claims/{id}/assessment : Demander expertise
- GET /v3/claims/{id}/settlement : Indemnisation
- POST /v3/claims/{id}/settlement : Approuver

Authentification : apiKey