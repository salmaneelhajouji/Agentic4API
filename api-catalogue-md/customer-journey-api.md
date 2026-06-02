# Customer Journey API (customer-journey-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Parcours client omnicanal. Reconstruction des chemins d'achat et points de friction.

## Endpoints
- GET /v1/journey/{customerId} : Parcours complet d'un client
- POST /v1/journey/touchpoints : Enregistrer un touchpoint
- GET /v1/journey/friction-points : Points de friction identifiés dans les parcours

Authentification : Clé API Kong Gateway — contacter votre équipe platform