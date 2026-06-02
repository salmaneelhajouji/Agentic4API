# Quality Control API (quality-control-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Controle qualite production. Plans de controle, mesures et non-conformites. DIFFERENCE vs data-quality-api : Quality Control = qualite produit physique, Data Quality = qualite donnees informatiques.

## Endpoints
- GET /v1/quality/plans : Plans de controle
- POST /v1/quality/plans : Creer
- GET /v1/quality/checks/{orderId} : Controles
- POST /v1/quality/checks/{orderId} : Realiser controle
- GET /v1/quality/nonconformities : Non-conformites
- POST /v1/quality/nonconformities : Declarer NC
- GET /v1/quality/nonconformities/{id} : Detail NC
- POST /v1/quality/nonconformities/{id} : Resoudre NC

Authentification : apiKey