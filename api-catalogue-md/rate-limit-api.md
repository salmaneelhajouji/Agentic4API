# Rate Limit API (rate-limit-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Gestion des quotas et limites de débit par client et endpoint.

## Endpoints
- GET /v1/rate-limits/{clientId} : Quotas d'un client
- PUT /v1/rate-limits/{clientId} : Modifier les quotas d'un client
- DELETE /v1/rate-limits/{clientId}/reset : Réinitialiser les compteurs
- POST /v1/rate-limits/blacklist : Blacklister un IP ou client

Authentification : Clé API Kong Gateway