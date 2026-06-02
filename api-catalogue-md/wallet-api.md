# Wallet API (wallet-api)
Version v1 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Portefeuille électronique interne. Crédits, rechargements et utilisation du solde plateforme. DIFFÉRENCE vs payment-api : Wallet = solde interne plateforme, Payment = transactions externes (carte/bank). Cas d'usage : crédits de remboursement, cashback, avoir en solde.

## Endpoints
- GET /v1/wallets/{userId} : Solde du portefeuille
- POST /v1/wallets/{userId}/topup : Recharger le portefeuille
- POST /v1/wallets/{userId}/debit : Débiter le portefeuille
- GET /v1/wallets/{userId}/transactions : Historique des transactions du portefeuille

Authentification : Clé API Kong Gateway