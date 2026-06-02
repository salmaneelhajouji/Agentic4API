# Loyalty Points API (loyalty-points-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe CRM

Programme de fidélité. Points accumulés, échangés et historique des récompenses.

## Endpoints
- GET /v1/loyalty/{customerId} : Solde de points fidélité
- POST /v1/loyalty/earn : Attribuer des points (après achat)
- POST /v1/loyalty/redeem : Utiliser des points (récompense)
- GET /v1/loyalty/{customerId}/history : Historique des transactions de fidélité
- GET /v1/loyalty/rewards : Catalogue des récompenses disponibles

Authentification : Clé API Kong Gateway