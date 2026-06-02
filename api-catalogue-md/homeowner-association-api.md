# Homeowner Association API (homeowner-association-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Gestion copropriété. Assemblées générales, charges et travaux.

## Endpoints
- GET /v1/hoa/{buildingId} : Info copropriété
- GET /v1/hoa/{buildingId}/meetings : AG planifiées
- POST /v1/hoa/{buildingId}/meetings : Créer AG
- GET /v1/hoa/{buildingId}/charges : Charges copropriété
- POST /v1/hoa/{buildingId}/charges : Appliquer charges
- GET /v1/hoa/{buildingId}/works : Travaux
- POST /v1/hoa/{buildingId}/works : Créer travaux

Authentification : apiKey