# Utility Management API (utility-management-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Gestion fluides et services. Eau, électricité, gaz et internet dans les logements.

## Endpoints
- GET /v1/utilities/{propertyId} : Services actifs
- POST /v1/utilities/{propertyId} : Activer service
- GET /v1/utilities/{propertyId}/readings : Relevés
- POST /v1/utilities/{propertyId}/readings : Soumettre relevé
- GET /v1/utilities/{propertyId}/invoices : Factures

Authentification : apiKey