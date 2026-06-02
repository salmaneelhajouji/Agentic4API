# Payment API (payment-api-v3)
Version v3 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Version 3 Payment. Paiements crypto, paiement en plusieurs fois (BNPL) et réconciliation bancaire automatique. DIFFÉRENCE vs v2 : ajout BNPL (Klarna/Alma), crypto (BTC/ETH), réconciliation.

## Endpoints
- POST /v3/payments : Initier un paiement (card/paypal/sepa/bnpl/crypto)
- POST /v3/payments/{id}/dispute : Contester un paiement (chargeback)
- POST /v3/payments/reconciliation : Lancer la réconciliation bancaire

Authentification : apiKey