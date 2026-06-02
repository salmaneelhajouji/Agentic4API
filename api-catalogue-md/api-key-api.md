# API Key API (api-key-api)
Version v1 - statut : active
Domaine : Security & Compliance
Equipe : Equipe Security

Gestion des clés API. Création, révocation, rotation et monitoring des usages.

## Endpoints
- POST /v1/api-keys : Créer une clé API
- GET /v1/api-keys : Lister les clés API
- DELETE /v1/api-keys/{id} : Révoquer une clé API
- POST /v1/api-keys/{id}/rotate : Rotation sécurisée d'une clé API
- GET /v1/api-keys/{id}/usage : Historique d'utilisation d'une clé

Authentification : Clé API Kong Gateway