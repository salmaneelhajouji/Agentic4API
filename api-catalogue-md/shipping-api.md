# Shipping API (shipping-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Expéditions et livraisons. Calcul des frais de port, tracking et retours. DIFFÉRENCE vs delivery-api : Shipping gère les colis et transporteurs, Delivery gère les créneaux de livraison planifiés.

## Endpoints
- POST /v1/shipping/estimate : Estimer les frais de livraison
- POST /v1/shipping/create : Créer une expédition
- GET /v1/shipping/{trackingId} : Suivre un colis
- PUT /v1/shipping/{trackingId}/cancel : Annuler une expédition
- POST /v1/shipping/return : Créer un retour colis

Authentification : Clé API Kong Gateway