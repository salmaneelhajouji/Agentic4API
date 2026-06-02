# MES API (mes-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Manufacturing Execution System. Supervision atelier, temps reel et KPIs.

## Endpoints
- GET /v1/mes/shop-floor : Etat atelier
- GET /v1/mes/workcenters : Postes de charge
- POST /v1/mes/workcenters : Ajouter
- GET /v1/mes/workcenters/{id} : TRS/OEE
- GET /v1/mes/events : Evenements production
- POST /v1/mes/events : Enregistrer

Authentification : apiKey