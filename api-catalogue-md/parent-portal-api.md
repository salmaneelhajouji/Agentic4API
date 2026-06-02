# Parent Portal API (parent-portal-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Espace parents. Suivi scolaire, communications et paiements.

## Endpoints
- GET /v1/parent/{parentId} : Informations parent
- GET /v1/parent/{parentId}/children : Progression enfants
- GET /v1/parent/{parentId}/messages : Messages
- POST /v1/parent/{parentId}/messages : Envoyer message
- GET /v1/parent/{parentId}/payments : Paiements scolarité

Authentification : apiKey