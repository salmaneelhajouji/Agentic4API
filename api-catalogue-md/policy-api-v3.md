# Policy API (policy-api-v3)
Version v3 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Contrats d'assurance complets. Souscription, avenants, renouvellement et résiliation.

## Endpoints
- GET /v3/policies : Portefeuille contrats
- POST /v3/policies : Souscrire contrat
- GET /v3/policies/{id} : Detail contrat
- PUT /v3/policies/{id} : Modifier
- GET /v3/policies/{id}/endorsements : Avenants
- POST /v3/policies/{id}/endorsements : Créer avenant
- GET /v3/policies/{id}/renewal : Info renouvellement
- POST /v3/policies/{id}/renewal : Renouveler
- POST /v3/policies/{id}/cancel : Résilier contrat

Authentification : apiKey