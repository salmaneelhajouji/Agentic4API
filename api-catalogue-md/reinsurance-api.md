# Reinsurance API (reinsurance-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Réassurance et cession de risques. Traités, facultatives et sinistres réassureurs.

## Endpoints
- GET /v1/reinsurance/treaties : Traités de réassurance
- POST /v1/reinsurance/treaties : Créer traité
- GET /v1/reinsurance/treaties/{id} : Detail traité
- PUT /v1/reinsurance/treaties/{id} : Modifier
- GET /v1/reinsurance/claims : Sinistres cédés
- POST /v1/reinsurance/claims : Céder sinistre

Authentification : apiKey