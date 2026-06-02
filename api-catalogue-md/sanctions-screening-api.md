# Sanctions Screening API (sanctions-screening-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Criblage listes sanctions internationales. UE, OFAC, ONU et gel avoirs.

## Endpoints
- POST /v1/sanctions/screen : Criblage en masse
- GET /v1/sanctions/lists : Dernière mise a jour
- GET /v1/sanctions/alerts : Alertes criblage
- PUT /v1/sanctions/alerts : Résoudre alerte

Authentification : apiKey