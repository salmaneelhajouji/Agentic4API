# Rent Collection API (rent-collection-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Collecte loyers et charges. Quittances, relances et comptabilité. DIFFERENCE vs billing-api : Rent Collection = loyers immobiliers avec quittances, Billing = abonnements et facturation générique.

## Endpoints
- GET /v1/rent/{leaseId} : Statut loyer
- POST /v1/rent/{leaseId} : Enregistrer paiement
- GET /v1/rent/{leaseId}/receipts : Quittances
- POST /v1/rent/{leaseId}/receipts : Générer quittance
- GET /v1/rent/{leaseId}/reminders : Relances
- POST /v1/rent/{leaseId}/reminders : Envoyer relance

Authentification : apiKey