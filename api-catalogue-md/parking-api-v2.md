# Parking API (parking-api-v2)
Version v2 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion parkings et stationnement. Disponibilité, réservation et paiement. DIFFERENCE vs ev-charging-api : Parking = stationnement generique, EV Charging = recharge véhicules électriques spécifiquement.

## Endpoints
- GET /v2/parking : Parkings disponibles
- POST /v2/parking : Réserver place
- GET /v2/parking/{id} : Disponibilité
- POST /v2/parking/{id}/payment : Payer stationnement

Authentification : apiKey