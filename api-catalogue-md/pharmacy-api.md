# Pharmacy API (pharmacy-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Stock pharmaceutique, dispensation et traçabilité médicaments. Alertes péremption et ruptures.

## Endpoints
- GET /v1/drugs : Stock médicaments
- POST /v1/drugs : Référencer
- GET /v1/drugs/{id} : Fiche médicament
- PUT /v1/drugs/{id} : Mise à jour stock
- GET /v1/dispensations : Historique
- POST /v1/dispensations : Dispenser

Authentification : apiKey