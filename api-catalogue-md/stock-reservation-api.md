# Stock Reservation API (stock-reservation-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Réservation temporaire de stock lors du checkout. DIFFÉRENCE vs inventory-api : Stock Reservation = verrouillage temporaire (pendant la session panier), Inventory = stocks globaux et historique mouvements. Évite les surventes.

## Endpoints
- POST /v1/stock/reserve : Réserver du stock temporairement (TTL 15 min)
- GET /v1/stock/reservations/{id} : Statut d'une réservation
- DELETE /v1/stock/reservations/{id} : Libérer la réservation
- POST /v1/stock/confirm/{reservationId} : Confirmer la réservation (stock déduit définitivement)

Authentification : Clé API Kong Gateway — contacter votre équipe platform