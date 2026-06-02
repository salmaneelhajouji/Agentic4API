# Payment API (payment-api)
Version v2 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Traitement des transactions de paiement ponctuelles. Carte bancaire, PayPal, virement SEPA, remboursements. DIFFÉRENCE vs billing-api : Payment traite UNE transaction, Billing gère les cycles récurrents. DIFFÉRENCE vs invoice-api : Payment effectue le paiement, Invoice génère le document fiscal. DIFFÉRENCE vs wallet-api : Payment traite les paiements externes (carte/bank), Wallet gère le solde interne.

## Endpoints
- POST /v2/payments : Initier un paiement
- GET /v2/payments/{id} : Statut d'un paiement
- POST /v2/payments/{id}/refund : Rembourser (total ou partiel)
- POST /v2/payments/capture : Capturer un paiement pré-autorisé
- GET /v2/payments?orderId={id} : Paiements d'une commande

Authentification : Clé API Kong Gateway