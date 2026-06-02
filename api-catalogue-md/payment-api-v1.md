# Payment API (payment-api-v1)
Version v1 - statut : deprecated
Domaine : Finance
Equipe : Equipe Finance

Version 1 de l'API paiement. DEPRECATED 2022. Supporte uniquement les paiements carte, pas de PayPal ni SEPA. Remboursements manuels uniquement. Migrer vers v2.

## Endpoints
- POST /v1/payments : Créer un paiement carte (seul canal supporté)
- GET /v1/payments/{id} : Statut du paiement
- DELETE /v1/payments/{id} : Annuler (BREAKING v2: remplacé par /refund)

Authentification : Clé API Kong Gateway — contacter votre équipe platform