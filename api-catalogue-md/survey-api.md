# Survey API (survey-api)
Version v1 - statut : active
Domaine : Customer Support
Equipe : Equipe Support

Enquêtes de satisfaction client. NPS, CSAT, création et analyse des résultats.

## Endpoints
- POST /v1/surveys : Créer une enquête
- POST /v1/surveys/{id}/send : Envoyer l'enquête à des clients
- POST /v1/surveys/{id}/respond : Soumettre une réponse
- GET /v1/surveys/{id}/results : Résultats de l'enquête
- GET /v1/surveys/nps : Score NPS global

Authentification : Clé API Kong Gateway