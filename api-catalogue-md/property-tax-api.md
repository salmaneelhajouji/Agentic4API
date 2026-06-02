# Property Tax API (property-tax-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Taxes foncières et impositions immobilières. Calcul, déclarations et suivi.

## Endpoints
- GET /v1/property-tax/{propertyId} : Taxe fonciere
- POST /v1/property-tax/{propertyId} : Calculer
- GET /v1/property-tax/{propertyId}/declarations : Déclarations
- POST /v1/property-tax/{propertyId}/declarations : Soumettre

Authentification : apiKey