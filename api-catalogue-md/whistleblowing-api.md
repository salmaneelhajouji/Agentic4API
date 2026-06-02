# Whistleblowing API (whistleblowing-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Signalement alerte ethique. Canal securise, anonymat et suivi. Loi Sapin II.

## Endpoints
- POST /v1/whistleblowing/alerts : Signaler anonymement
- GET /v1/whistleblowing/alerts : Signalements recus
- GET /v1/whistleblowing/alerts/{id} : Statut signalement
- POST /v1/whistleblowing/alerts/{id} : Mettre a jour
- GET /v1/whistleblowing/config : Config canal
- PUT /v1/whistleblowing/config : Modifier

Authentification : apiKey