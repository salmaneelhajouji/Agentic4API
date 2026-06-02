# Transfer API (transfer-api-v2)
Version v2 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Virements SEPA, SWIFT et instantane. DIFFERENCE vs payout-api : Transfer = virement entre comptes bancaires, Payout = reversement plateforme vers vendeur.

## Endpoints
- GET /v2/transfers : Historique
- POST /v2/transfers : Creer virement
- GET /v2/transfers/{id} : Statut
- DELETE /v2/transfers/{id} : Annuler
- POST /v2/transfers/validate-iban : Valider IBAN
- POST /v2/transfers/fees : Calculer frais

Authentification : apiKey