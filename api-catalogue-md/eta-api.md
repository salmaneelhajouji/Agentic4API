# ETA API (eta-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Calcul temps d'arrivée estimé. Trafic temps réel, conditions météo et historique. DIFFERENCE vs route-optimization-api : ETA = estimation heure arrivee, Route = calcul itineraire optimal.

## Endpoints
- POST /v1/eta/calculate : Calculer ETA
- GET /v1/eta/{shipmentId} : ETA livraison
- PUT /v1/eta/{shipmentId} : Mettre a jour ETA
- GET /v1/eta/history/{routeId} : Précision historique ETA

Authentification : apiKey