# Claims Notification API (claims-notification-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Notifications sinistres. Alertes clients et partenaires. DIFFERENCE vs notification-api : Claims Notification = alertes specifiques assurance sinistre, Notification = multi-canaux generique.

## Endpoints
- GET /v1/claims-notifications/{claimId} : Notifications envoyees
- POST /v1/claims-notifications/{claimId} : Envoyer notification

Authentification : apiKey