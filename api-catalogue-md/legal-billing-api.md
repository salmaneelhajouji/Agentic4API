# Legal Billing API (legal-billing-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Facturation cabinet d'avocats. Honoraires, temps passe et notes de frais. DIFFERENCE vs billing-api : Legal Billing = honoraires avocats/notaires (temps passe, forfait), Billing = facturation services generiques.

## Endpoints
- GET /v1/legal-billing/matters/{matterId} : Facturation dossier
- POST /v1/legal-billing/matters/{matterId} : Saisir temps
- GET /v1/legal-billing/invoices : Factures
- POST /v1/legal-billing/invoices : Générer facture
- GET /v1/legal-billing/invoices/{id} : Detail
- POST /v1/legal-billing/invoices/{id} : Envoyer

Authentification : apiKey