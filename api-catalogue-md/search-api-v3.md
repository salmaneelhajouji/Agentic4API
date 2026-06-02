# Search API (search-api-v3)
Version v3 - statut : active
Domaine : E-Commerce
Equipe : Equipe Platform

Version actuelle. Introduit la recherche conversationnelle (LLM), les synonymes configurables, le merchandising et le ranking A/B en production. DIFFÉRENCE vs search-api-v2 : v3 ajoute la couche LLM pour les requêtes en langage naturel et le merchandising manuel.

## Endpoints
- GET /v3/search : Recherche hybride + LLM conversationnelle
- POST /v3/search/synonyms : Créer un dictionnaire de synonymes (nouveau en v3)
- GET /v3/search/synonyms : Lister les dictionnaires
- POST /v3/search/merchandising : Créer règle de merchandising (boost/bury — nouveau en v3)
- GET /v3/search/analytics : Analytics de recherche (requêtes sans résultat, taux de clic)

Authentification : Clé API Kong Gateway — Devoteam nexDigital