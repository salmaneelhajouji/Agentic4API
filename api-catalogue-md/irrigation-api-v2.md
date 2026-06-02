# Irrigation API (irrigation-api-v2)
Version v2 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Gestion systèmes d'irrigation. Programmation, consommation eau et optimisation.

## Endpoints
- GET /v2/irrigation/{fieldId} : Statut irrigation
- POST /v2/irrigation/{fieldId} : Arrêter
- GET /v2/irrigation/{fieldId}/schedule : Planning
- PUT /v2/irrigation/{fieldId}/schedule : Modifier
- GET /v2/irrigation/{fieldId}/consumption : Consommation eau

Authentification : apiKey