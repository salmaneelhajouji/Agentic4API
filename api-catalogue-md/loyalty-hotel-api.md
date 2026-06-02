# Loyalty Hotel API (loyalty-hotel-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Programme fidélité hôtelier. Points, statuts et avantages. DIFFERENCE vs loyalty-points-api : Loyalty Hotel = programme fidélité hôtel (nuitées, upgrades), Loyalty Points = programme fidélité commerce générique.

## Endpoints
- GET /v1/loyalty/hotel/{memberId} : Compte fidelite
- POST /v1/loyalty/hotel/{memberId} : Gagner points
- GET /v1/loyalty/hotel/{memberId}/status : Avantages statut

Authentification : apiKey