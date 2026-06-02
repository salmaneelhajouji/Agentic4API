# Driver API (driver-api-v2)
Version v2 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion conducteurs. Permis, scores de conduite et tachygraphe. DIFFERENCE vs employee-api : Driver = données spécifiques conducteurs (permis, infractions), Employee = données RH génériques.

## Endpoints
- GET /v2/drivers : Lister conducteurs
- POST /v2/drivers : Ajouter conducteur
- GET /v2/drivers/{id} : Profile conducteur
- PUT /v2/drivers/{id} : Modifier
- GET /v2/drivers/{id}/license : Permis de conduire
- PUT /v2/drivers/{id}/license : Mettre a jour
- GET /v2/drivers/{id}/score : Score de conduite

Authentification : apiKey