# Mortgage API (mortgage-api-v2)
Version v2 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Prets immobiliers avec hypotheque. Tableau d'amortissement et mainlevee. DIFFERENCE vs loan-api : Mortgage = credit immobilier avec garantie, Loan = pret sans garantie.

## Endpoints
- GET /v2/mortgages : Portefeuille
- POST /v2/mortgages : Demander
- GET /v2/mortgages/{id} : Dossier complet
- PUT /v2/mortgages/{id} : Modifier
- GET /v2/mortgages/{id}/amortization : Tableau amortissement
- POST /v2/mortgages/{id}/discharge : Mainlevee hypotheque

Authentification : apiKey