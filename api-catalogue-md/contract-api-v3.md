# Contract API (contract-api-v3)
Version v3 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Gestion contrats complets. Templates, negociation, signature et suivi. DIFFERENCE vs lease-api : Contract = contrat juridique generique, Lease = bail immobilier specifique.

## Endpoints
- GET /v3/contracts : Portefeuille contrats
- POST /v3/contracts : Créer contrat
- GET /v3/contracts/{id} : Detail
- PUT /v3/contracts/{id} : Modifier
- DELETE /v3/contracts/{id} : Terminer
- GET /v3/contracts/{id}/clauses : Clauses
- POST /v3/contracts/{id}/clauses : Ajouter clause
- POST /v3/contracts/{id}/sign : Signer
- GET /v3/contracts/{id}/sign : Statut signatures
- GET /v3/contracts/{id}/amendments : Avenants
- POST /v3/contracts/{id}/amendments : Créer avenant

Authentification : apiKey