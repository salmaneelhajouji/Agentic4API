# Billing API (billing-api)
Version v1 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Cycles de facturation récurrents et abonnements. Prélèvements automatiques, relances impayés, gestion des plans. DIFFÉRENCE vs payment-api : Billing orchestre des paiements récurrents dans le temps, Payment traite une transaction ponctuelle. DIFFÉRENCE vs invoice-api : Billing déclenche les cycles, Invoice génère les PDFs. DIFFÉRENCE vs subscription-api : Billing gère le paiement, Subscription gère les droits d'accès.

## Endpoints
- POST /v1/billing/subscriptions : Créer un abonnement récurrent
- GET /v1/billing/subscriptions/{customerId} : Abonnements actifs d'un client
- PUT /v1/billing/subscriptions/{id}/cancel : Résilier un abonnement
- GET /v1/billing/invoices/{customerId} : Historique des factures
- POST /v1/billing/retry/{invoiceId} : Relancer un paiement impayé

Authentification : Clé API Kong Gateway