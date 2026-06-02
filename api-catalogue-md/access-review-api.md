# Access Review API (access-review-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Revue des accès et habilitations. Campagnes de certification et nettoyage.

## Endpoints
- GET /v1/access-reviews : Campagnes revue
- POST /v1/access-reviews : Lancer campagne
- GET /v1/access-reviews/{id} : Detail campagne
- PUT /v1/access-reviews/{id} : Mettre a jour
- GET /v1/access-reviews/{id}/decisions : Décisions
- POST /v1/access-reviews/{id}/decisions : Soumettre décision
- GET /v1/access-reviews/{id}/remediation : Actions correctives

Authentification : apiKey