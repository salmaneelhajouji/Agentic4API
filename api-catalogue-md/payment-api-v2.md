# Payment API (payment-api-v2)
Version v2 - statut : deprecated
Domaine : Finance
Equipe : Equipe Finance

Version 2 de l'API paiement — DEPRECATED depuis 2024, migrer vers v3. Introduit PayPal et SEPA, le mode capture manuelle et les remboursements partiels. Incompatible avec v1 (ID integer → string PAY-XXXX).

## Endpoints
- POST /v2/payments : Initier paiement (card/PayPal/SEPA)
- GET /v2/payments : Lister les paiements
- GET /v2/payments/{id} : Statut d'un paiement
- POST /v2/payments/{id}/capture : Capturer un paiement pré-autorisé (mode manual)
- POST /v2/payments/{id}/refund : Remboursement total ou partiel

Authentification : Clé API Kong Gateway — Devoteam nexDigital