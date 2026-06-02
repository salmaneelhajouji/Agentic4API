# Livestock API (livestock-api-v2)
Version v2 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Gestion élevage. Identification animaux, santé et traçabilité.

## Endpoints
- GET /v2/livestock : Troupeau
- POST /v2/livestock : Enregistrer animal
- GET /v2/livestock/{id} : Fiche animal
- PUT /v2/livestock/{id} : Modifier
- GET /v2/livestock/{id}/health : Suivi santé
- POST /v2/livestock/{id}/health : Enregistrer événement
- GET /v2/livestock/{id}/movements : Mouvements

Authentification : apiKey