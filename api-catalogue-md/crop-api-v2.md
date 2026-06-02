# Crop API (crop-api-v2)
Version v2 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Gestion cultures et récoltes. Stades phénologiques, rendements et prévisions.

## Endpoints
- GET /v2/crops : Cultures en cours
- POST /v2/crops : Créer culture
- GET /v2/crops/{id} : Detail culture
- PUT /v2/crops/{id} : Modifier
- GET /v2/crops/{id}/phenology : Stade phénologique
- GET /v2/crops/{id}/yield : Rendement réel
- POST /v2/crops/{id}/yield : Prévoir rendement

Authentification : apiKey