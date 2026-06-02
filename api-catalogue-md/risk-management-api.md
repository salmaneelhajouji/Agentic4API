# Risk Management API (risk-management-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Gestion risques cybersécurité. Identification, évaluation et traitement.

## Endpoints
- GET /v1/risks : Risques identifiés
- POST /v1/risks : Créer risque
- GET /v1/risks/{id} : Detail risque
- PUT /v1/risks/{id} : Mettre a jour
- GET /v1/risks/{id}/treatment : Plan traitement
- POST /v1/risks/{id}/treatment : Appliquer traitement
- GET /v1/risks/heatmap : Cartographie risques

Authentification : apiKey