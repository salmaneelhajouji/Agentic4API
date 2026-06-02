# Production Order API (production-order-api-v3)
Version v3 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Ordres de fabrication complets. Gammes, nomenclatures, suivi et tracing. DIFFERENCE vs order-management-api : Production Order = OF industriel avec gammes/ressources, Order Management = commande commerciale client.

## Endpoints
- GET /v3/orders : Ordres de fabrication
- POST /v3/orders : Creer OF
- GET /v3/orders/{id} : Detail OF
- PUT /v3/orders/{id} : Modifier
- POST /v3/orders/{id} : Cloturer
- GET /v3/orders/{id}/operations : Gamme
- POST /v3/orders/{id}/operations : Ajouter operation
- GET /v3/orders/{id}/materials : Nomenclature
- POST /v3/orders/{id}/materials : Declarer consommation

Authentification : apiKey