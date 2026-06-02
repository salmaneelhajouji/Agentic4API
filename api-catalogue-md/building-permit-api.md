# Building Permit API (building-permit-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Permis de construire et autorisations urbanisme. Dépôt, suivi et conformité.

## Endpoints
- GET /v1/permits : Lister permis
- POST /v1/permits : Déposer demande
- GET /v1/permits/{id} : Statut instruction
- PUT /v1/permits/{id} : Modifier
- GET /v1/permits/{id}/documents : Documents
- POST /v1/permits/{id}/documents : Ajouter document

Authentification : apiKey