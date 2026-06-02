# Harvest API (harvest-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Planification et suivi des récoltes. Dates optimales, équipements et tonnages.

## Endpoints
- GET /v1/harvests : Récoltes planifiées
- POST /v1/harvests : Planifier récolte
- GET /v1/harvests/{id} : Detail
- PUT /v1/harvests/{id} : Modifier
- POST /v1/harvests/{id} : Terminer récolte
- GET /v1/harvests/{id}/tonnage : Tonnage récolté
- POST /v1/harvests/{id}/tonnage : Enregistrer

Authentification : apiKey