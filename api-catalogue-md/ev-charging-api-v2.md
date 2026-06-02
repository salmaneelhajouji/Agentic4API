# EV Charging API (ev-charging-api-v2)
Version v2 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Bornes recharge VE. Disponibilité temps réel, réservation et facturation. DIFFERENCE vs parking-api : EV Charging = recharge vehicules electriques, Parking = stationnement generique.

## Endpoints
- GET /v2/stations : Stations disponibles
- POST /v2/stations : Enregistrer
- GET /v2/stations/{id} : Disponibilite
- POST /v2/stations/{id}/session : Démarrer recharge
- DELETE /v2/stations/{id}/session : Arreter
- GET /v2/stations/{id}/history : Historique recharges

Authentification : apiKey