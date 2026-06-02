# Court Filing API (court-filing-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Dépôts et actes au tribunal. RPVA, e-barreau et suivi.

## Endpoints
- GET /v1/filings : Dépôts en cours
- POST /v1/filings : Créer dépôt
- GET /v1/filings/{id} : Statut
- POST /v1/filings/{id} : Soumettre
- GET /v1/filings/{id}/documents : Documents
- POST /v1/filings/{id}/documents : Ajouter

Authentification : apiKey