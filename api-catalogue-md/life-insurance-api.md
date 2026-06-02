# Life Insurance API (life-insurance-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Assurance vie et prévoyance. Contrats, rachats et désignation bénéficiaires.

## Endpoints
- GET /v1/life-insurance : Contrats vie
- POST /v1/life-insurance : Souscrire
- GET /v1/life-insurance/{contractId} : Detail contrat
- PUT /v1/life-insurance/{contractId} : Modifier
- GET /v1/life-insurance/{contractId}/beneficiaries : Bénéficiaires
- POST /v1/life-insurance/{contractId}/beneficiaries : Ajouter bénéficiaire
- GET /v1/life-insurance/{contractId}/surrender : Valeur de rachat
- POST /v1/life-insurance/{contractId}/surrender : Demander rachat

Authentification : apiKey