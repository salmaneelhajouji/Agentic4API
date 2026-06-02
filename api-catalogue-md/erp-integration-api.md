# ERP Integration API (erp-integration-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Integration ERP SAP/Oracle. Synchronisation donnees et transactions.

## Endpoints
- POST /v1/erp/sync : Synchroniser donnees referentielles
- GET /v1/erp/sync : Statut synchronisation
- GET /v1/erp/purchase-orders : Commandes achat ERP
- POST /v1/erp/purchase-orders : Creer commande achat
- GET /v1/erp/invoices : Factures ERP
- POST /v1/erp/invoices : Comptabiliser facture

Authentification : apiKey