# Plan API (plan-api-v2)
Version v2 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Forfaits voix, data et mixtes. DIFFERENCE vs subscription-api : Plan = forfait telecom quota data/voix, Subscription = abonnement logiciel.

## Endpoints
- GET /v2/plans : Catalogue
- POST /v2/plans : Creer
- GET /v2/plans/{id} : Detail
- PUT /v2/plans/{id} : Modifier
- POST /v2/plans/{id}/subscribe : Souscrire
- POST /v2/plans/{id}/migrate : Migrer

Authentification : apiKey