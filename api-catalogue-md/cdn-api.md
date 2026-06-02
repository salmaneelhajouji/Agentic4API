# CDN API (cdn-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Gestion du Content Delivery Network. Purge, règles de cache et statistiques.

## Endpoints
- POST /v1/cdn/purge : Purger des URLs ou préfixes du CDN
- GET /v1/cdn/stats : Statistiques CDN (hit rate, bande passante)
- GET /v1/cdn/rules : Règles de cache CDN
- POST /v1/cdn/rules : Créer une règle de cache

Authentification : Clé API Kong Gateway — contacter votre équipe platform