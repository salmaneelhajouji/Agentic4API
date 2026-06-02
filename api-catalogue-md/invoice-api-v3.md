# Invoice API (invoice-api-v3)
Version v3 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Version 3 de l'API facture — version actuelle recommandée. Ajout de la facturation récurrente native, des pénalités de retard automatiques et de l'intégration comptable (exports FEC, DATEV). DIFFÉRENCE vs billing-api : Invoice génère et archive les documents fiscaux légaux, Billing orchestre les prélèvements automatiques.

## Endpoints
- POST /v3/invoices : Générer facture avec récurrence et export comptable
- GET /v3/invoices : Lister factures avec filtres avancés
- GET /v3/invoices/{id} : Facture complète avec statut pénalité
- GET /v3/invoices/{id}/pdf : PDF multilingue, signé eIDAS si B2B > 10k€
- GET /v3/invoices/{id}/accounting-export : Export comptable (FEC / DATEV / SAGE / CEGID) — nouveau en v3
- POST /v3/invoices/{id}/penalty : Appliquer manuellement une pénalité de retard
- PUT /v3/invoices/{id}/void : Annuler (génère avoir + pénalité réversée si applicable)

Authentification : Clé API Kong Gateway — Devoteam nexDigital