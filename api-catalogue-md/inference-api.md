# Inference API (inference-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Serving inference ML. DIFFERENCE vs model-registry-api : Inference = execution predictions, Model Registry = gestion versions.

## Endpoints
- POST /v1/inference/{modelId} : Prediction
- GET /v1/inference/{modelId} : Info modele
- POST /v1/inference/batch : Batch
- GET /v1/inference/batch : Statut

Authentification : apiKey