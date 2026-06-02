# Field API (field-api-v2)
Version v2 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Gestion parcelles agricoles. Cartographie, sol et historique cultural.

## Endpoints
- GET /v2/fields : Lister parcelles
- POST /v2/fields : Créer parcelle
- GET /v2/fields/{id} : Detail parcelle
- PUT /v2/fields/{id} : Modifier
- GET /v2/fields/{id}/soil : Données sol
- POST /v2/fields/{id}/soil : Ajouter analyse
- GET /v2/fields/{id}/history : Historique cultural

Authentification : apiKey