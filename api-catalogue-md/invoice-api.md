# Invoice API (invoice-api)
Version v1 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Génération de documents de facturation conformes. Factures, avoirs, notes de débit en PDF. DIFFÉRENCE vs payment-api : Invoice = document fiscal APRÈS paiement, Payment = transaction. DIFFÉRENCE vs billing-api : Invoice = PDFs envoyés aux clients, Billing = prélèvements automatiques. Cas d'usage : facture après commande payée, avoir après remboursement.

## Endpoints
- POST /v1/invoices : Générer une facture
- GET /v1/invoices/{id} : Récupérer une facture
- GET /v1/invoices/{id}/pdf : Télécharger en PDF
- POST /v1/invoices/{id}/send : Envoyer par email au client
- PUT /v1/invoices/{id}/void : Annuler une facture (génère un avoir automatiquement)

Authentification : Clé API Kong Gateway