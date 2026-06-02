# Shipping API (shipping-api-v2)
Version v2 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Version 2 de l'API d'expédition — version actuelle recommandée. Ajout du tracking temps réel GPS, des expéditions multi-colis, de la gestion des douanes pour l'export international et du calcul CO2. DIFFÉRENCE vs delivery-api : Shipping gère les colis et transporteurs, Delivery gère les créneaux et plannings de livraison.

## Endpoints
- POST /v2/shipping/create : Créer expédition multi-colis avec calcul CO2 et douanes
- POST /v2/shipping/estimate : Estimer frais et CO2 par transporteur
- GET /v2/shipping/{id} : Statut complet de l'expédition
- GET /v2/shipping/{id}/live-track : Tracking GPS temps réel (WebSocket SSE — nouveau en v2)
- GET /v2/shipping/{id}/labels : Étiquettes en PDF ou ZPL (nouveau format en v2)
- PUT /v2/shipping/{id}/cancel : Annuler une expédition

Authentification : Clé API Kong Gateway — Devoteam nexDigital