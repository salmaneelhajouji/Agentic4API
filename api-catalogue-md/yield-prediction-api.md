# Yield Prediction API (yield-prediction-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Prévisions rendements par IA. Modèles satellites et météo. DIFFERENCE vs crop-api : Yield Prediction = modèle prédictif ML, Crop = données réelles cultures.

## Endpoints
- GET /v1/yield/{fieldId} : Prédiction rendement
- POST /v1/yield/{fieldId} : Lancer modèle
- GET /v1/yield/{fieldId}/scenarios : Scénarios prédiction

Authentification : apiKey