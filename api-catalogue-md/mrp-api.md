# MRP API (mrp-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Material Requirements Planning. Calcul besoins, suggestions et lancement. DIFFERENCE vs inventory-api : MRP = calcul besoins futurs selon planification, Inventory = stock physique actuel.

## Endpoints
- POST /v1/mrp/calculate : Calculer besoins MRP
- GET /v1/mrp/suggestions : Suggestions approvisionnement
- POST /v1/mrp/suggestions : Accepter suggestion
- GET /v1/mrp/plan/{productId} : Plan de production

Authentification : apiKey