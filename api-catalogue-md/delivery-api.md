# Delivery API (delivery-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Créneaux de livraison et planning. Réservation de plages horaires et gestion des livreurs. DIFFÉRENCE vs shipping-api : Delivery = planning des créneaux et livreurs, Shipping = colis et transporteurs.

## Endpoints
- GET /v1/delivery/slots : Créneaux de livraison disponibles
- POST /v1/delivery/book : Réserver un créneau de livraison
- PUT /v1/delivery/{id}/reschedule : Modifier le créneau de livraison
- GET /v1/delivery/tracking/{id} : Suivi en temps réel du livreur

Authentification : Clé API Kong Gateway