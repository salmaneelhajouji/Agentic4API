# Loan API (loan-api-v3)
Version v3 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Prets personnels et professionnels. Decision IA et echeancier. DIFFERENCE vs mortgage-api : Loan = pret personnel sans garantie, Mortgage = pret immobilier avec hypotheque.

## Endpoints
- GET /v3/loans : Portefeuille
- POST /v3/loans : Demander
- GET /v3/loans/{id} : Detail
- PUT /v3/loans/{id} : Modifier
- GET /v3/loans/{id}/repayments : Echeancier
- POST /v3/loans/{id}/repayments : Rembourser
- POST /v3/loans/simulate : Simuler
- POST /v3/loans/{id}/early-repayment : Remboursement anticipe

Authentification : apiKey