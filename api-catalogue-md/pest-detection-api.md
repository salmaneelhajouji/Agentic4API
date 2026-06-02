# Pest Detection API (pest-detection-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Détection ravageurs et maladies. Identification IA par photo et traitements recommandés.

## Endpoints
- POST /v1/pests/detect : Identifier ravageur/maladie par photo
- GET /v1/pests/{fieldId}/monitoring : Surveillance active
- POST /v1/pests/{fieldId}/monitoring : Signaler observation
- GET /v1/pests/treatments : Traitements disponibles
- POST /v1/pests/treatments : Recommander traitement

Authentification : apiKey