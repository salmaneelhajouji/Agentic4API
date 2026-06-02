# Renewal API (renewal-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Renouvellements contrats. Notifications, négociation et confirmation.

## Endpoints
- GET /v1/renewals : Renouvellements à venir
- POST /v1/renewals : Traiter renouvellement
- GET /v1/renewals/{contractId} : Statut renouvellement
- POST /v1/renewals/{contractId} : Négocier conditions

Authentification : apiKey