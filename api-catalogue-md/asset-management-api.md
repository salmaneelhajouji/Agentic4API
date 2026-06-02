# Asset-Management API (asset-management-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Gestion actifs industriels. Immobilisations, amortissements et valeur residuelle. DIFFERENCE vs asset-tracking-api : Asset Management = valeur et comptabilite immobilisations, Asset Tracking = position GPS actifs.

## Endpoints
- GET /v1/assets-mgmt : Actifs
- POST /v1/assets-mgmt : Ajouter
- GET /v1/assets-mgmt/{id} : Detail
- PUT /v1/assets-mgmt/{id} : Modifier
- GET /v1/assets-mgmt/{id}/depreciation : Amortissement
- POST /v1/assets-mgmt/{id}/depreciation : Calculer

Authentification : apiKey