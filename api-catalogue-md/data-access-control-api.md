# Data Access Control API (data-access-control-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Controle acces donnees. RBAC, policies et audits acces. DIFFERENCE vs permission-api : Data Access Control = droits sur datasets, Permission = droits applicatifs generiques.

## Endpoints
- GET /v1/data-access/policies : Politiques acces
- POST /v1/data-access/policies : Creer
- GET /v1/data-access/{datasetId}/grants : Droits accordes
- POST /v1/data-access/{datasetId}/grants : Accorder acces
- DELETE /v1/data-access/{datasetId}/grants : Revoquer acces

Authentification : apiKey