# Bank Account API (bank-account-api-v3)
Version v3 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Comptes courants et epargne avec open banking PSD2. DIFFERENCE vs wallet-api : Bank Account = compte bancaire IBAN/RIB, Wallet = portefeuille electronique interne.

## Endpoints
- GET /v3/accounts : Lister
- POST /v3/accounts : Ouvrir
- GET /v3/accounts/{id} : Detail
- PUT /v3/accounts/{id} : Modifier
- DELETE /v3/accounts/{id} : Cloturer
- GET /v3/accounts/{id}/transactions : Releve
- POST /v3/accounts/{id}/transactions : Initier

Authentification : apiKey