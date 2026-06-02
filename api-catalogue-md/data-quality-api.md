# Data Quality API (data-quality-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Qualite des donnees. Regles et anomalies. DIFFERENCE vs data-catalog-api : Data Quality = controles qualite, Data Catalog = gouvernance inventaire.

## Endpoints
- GET /v1/quality/rules : Regles
- POST /v1/quality/rules : Creer
- POST /v1/quality/checks/{datasetId} : Lancer
- GET /v1/quality/checks/{datasetId} : Resultats
- GET /v1/quality/anomalies : Anomalies
- PUT /v1/quality/anomalies : Acquitter

Authentification : apiKey