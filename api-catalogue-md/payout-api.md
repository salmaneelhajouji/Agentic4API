# Payout API (payout-api)
Version v1 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Versements aux vendeurs et partenaires. Marketplace payouts, virements SEPA et suivi. DIFFÉRENCE vs payment-api : Payout = versement DE nous VERS un tiers (vendeur, partenaire), Payment = encaissement D'un client VERS nous.

## Endpoints
- POST /v1/payouts : Créer un virement vers un bénéficiaire
- GET /v1/payouts : Lister les virements
- GET /v1/payouts/{id} : Statut d'un virement
- POST /v1/payouts/batch : Virement en masse (max 1000)

Authentification : apiKey