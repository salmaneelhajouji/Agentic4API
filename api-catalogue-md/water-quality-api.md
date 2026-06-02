# Water Quality API (water-quality-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Qualite eau irrigation. Analyses, parametres et conformite. DIFFERENCE vs air-quality-api : Water Quality = eau usage agricole, Air Quality = qualite air.

## Endpoints
- GET /v1/water-quality/{sourceId} : Parametres eau
- POST /v1/water-quality/{sourceId} : Ajouter analyse
- GET /v1/water-quality/{sourceId}/compliance : Conformite

Authentification : apiKey