# Soil Analysis API (soil-analysis-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Analyses de sol. pH, nutriments et recommandations fertilisation. DIFFERENCE vs field-api : Soil Analysis = analyses laboratoire ponctuelles, Field = gestion parcelle complète.

## Endpoints
- GET /v1/soil/analyses : Analyses en cours
- POST /v1/soil/analyses : Commander analyse
- GET /v1/soil/analyses/{id} : Recommandations fertilisation

Authentification : apiKey