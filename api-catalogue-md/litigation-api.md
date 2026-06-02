# Litigation API (litigation-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Gestion des litiges et contentieux. Dossiers, procedures et suivi judiciaire.

## Endpoints
- GET /v1/litigation : Dossiers contentieux
- POST /v1/litigation : Ouvrir dossier
- GET /v1/litigation/{id} : Detail dossier
- PUT /v1/litigation/{id} : Mettre a jour
- GET /v1/litigation/{id}/hearings : Audiences
- POST /v1/litigation/{id}/hearings : Planifier audience
- GET /v1/litigation/{id}/documents : Documents
- POST /v1/litigation/{id}/documents : Ajouter

Authentification : apiKey