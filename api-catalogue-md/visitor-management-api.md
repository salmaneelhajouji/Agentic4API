# Visitor Management API (visitor-management-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Gestion visiteurs et accès immeubles. Badges, invitations et journal des accès.

## Endpoints
- GET /v1/visitors : Visiteurs du jour
- POST /v1/visitors : Pré-enregistrer
- GET /v1/visitors/{id} : Detail
- POST /v1/visitors/{id} : Enregistrer sortie
- GET /v1/visitors/access-log : Journal des accès

Authentification : apiKey