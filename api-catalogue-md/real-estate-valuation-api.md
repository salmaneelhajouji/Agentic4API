# Real Estate Valuation API (real-estate-valuation-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Valorisation immobilière par IA. Estimation, comparables et tendances. DIFFERENCE vs property-api : Valuation = estimation valeur marché, Property = fiche descriptive du bien.

## Endpoints
- POST /v1/valuation/estimate : Estimer valeur marche
- GET /v1/valuation/{propertyId} : Valorisation bien
- POST /v1/valuation/comparables : Biens comparables

Authentification : apiKey