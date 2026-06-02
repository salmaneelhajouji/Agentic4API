# Config API (config-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Configuration applicative et feature flags.

## Endpoints
- GET /v1/config/{key} : Récupérer une configuration
- PUT /v1/config/{key} : Définir une configuration
- GET /v1/config/features : Lister les feature flags
- PUT /v1/config/features/{flag}/toggle : Activer/désactiver un feature flag

Authentification : Clé API Kong Gateway