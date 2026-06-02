# Intellectual Property API (intellectual-property-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Propriete intellectuelle. Brevets, marques, droits d'auteur et litiges.

## Endpoints
- GET /v1/ip/assets : Actifs PI
- POST /v1/ip/assets : Deposer
- GET /v1/ip/assets/{id} : Detail actif PI
- PUT /v1/ip/assets/{id} : Renouveler
- DELETE /v1/ip/assets/{id} : Abandonner
- GET /v1/ip/assets/{id}/licenses : Licences
- POST /v1/ip/assets/{id}/licenses : Créer licence
- POST /v1/ip/search : Rechercher conflits

Authentification : apiKey