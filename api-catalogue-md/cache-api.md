# Cache API (cache-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Gestion du cache distribué. Lecture, écriture, invalidation et TTL.

## Endpoints
- GET /v1/cache/{key} : Lire une valeur en cache
- PUT /v1/cache/{key} : Écrire une valeur en cache
- DELETE /v1/cache/{key} : Invalider une clé de cache
- DELETE /v1/cache/invalidate-prefix : Invalider toutes les clés avec un préfixe
- GET /v1/cache/stats : Statistiques du cache (hit rate, mémoire)

Authentification : Clé API Kong Gateway — contacter votre équipe platform