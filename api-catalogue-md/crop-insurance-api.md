# Crop Insurance API (crop-insurance-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Assurance récoltes. Grêle, sécheresse et sinistres. DIFFERENCE vs insurance-claim-api : Crop Insurance = assurance récolte agricole, Claim = sinistre assurance générique.

## Endpoints
- GET /v1/crop-insurance/contracts : Contrats récolte
- POST /v1/crop-insurance/contracts : Souscrire
- GET /v1/crop-insurance/claims : Sinistres récolte
- POST /v1/crop-insurance/claims : Déclarer perte

Authentification : apiKey