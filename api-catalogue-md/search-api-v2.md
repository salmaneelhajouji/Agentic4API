# Search API (search-api-v2)
Version v2 - statut : active
Domaine : E-Commerce
Equipe : Equipe Platform

Version 2 Search. Recherche sémantique vectorielle, personnalisation par profil et A/B sur le ranking. DIFFÉRENCE vs v1 : v2 ajoute embedding vectoriel, personnalisation et expérimentation sur les résultats.

## Endpoints
- GET /v2/search : Recherche hybride (lexical + sémantique)
- POST /v2/search/similar : Recherche par similarité (more-like-this)
- POST /v2/search/reindex : Forcer une réindexation complète ou partielle

Authentification : apiKey