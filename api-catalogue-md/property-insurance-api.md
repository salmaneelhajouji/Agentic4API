# Property Insurance API (property-insurance-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Assurance habitation et biens. MRH, garanties et sinistres. DIFFERENCE vs property-api (immobilier) : Property Insurance = contrat assurance bien, Property = fiche descriptive du bien.

## Endpoints
- GET /v1/property-insurance : Contrats habitation
- POST /v1/property-insurance : Souscrire MRH
- GET /v1/property-insurance/{contractId} : Detail contrat
- PUT /v1/property-insurance/{contractId} : Modifier
- GET /v1/property-insurance/{contractId}/guarantees : Garanties incluses

Authentification : apiKey