# Invoice API (invoice-api-v2)
Version v2 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Version 2 de la facture. Ajout des avoirs (credit notes), facturation en plusieurs langues et signature électronique. DIFFÉRENCE vs v1 : credit_note automatique à l'annulation, multi-devises natif, signature eIDAS.

## Endpoints
- POST /v2/invoices : Générer une facture multilingue et multi-devise
- GET /v2/invoices/{id} : Récupérer une facture
- GET /v2/invoices/{id}/pdf : PDF facture dans la langue configurée
- PUT /v2/invoices/{id}/void : Annuler (génère automatiquement un avoir/credit_note)
- GET /v2/invoices/{id}/credit-notes : Avoirs liés à cette facture
- POST /v2/invoices/{id}/sign : Signer électroniquement (eIDAS)

Authentification : Clé API Kong Gateway — contacter votre équipe platform