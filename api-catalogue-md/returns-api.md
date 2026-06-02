# Returns API (returns-api)
Version v1 - statut : active
Domaine : Retail
Equipe : Equipe Retail

Retours et remboursements. SAV, labels retour et reintegration stock.

## Endpoints
- GET /v1/returns : Retours en cours
- POST /v1/returns : Initier retour
- GET /v1/returns/{id} : Detail retour
- PUT /v1/returns/{id} : Mettre a jour statut
- GET /v1/returns/{id}/label : Label retour
- POST /v1/returns/{id}/label : Générer
- POST /v1/returns/{id}/refund : Traiter remboursement

Authentification : apiKey