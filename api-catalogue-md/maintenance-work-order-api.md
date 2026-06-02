# Maintenance Work Order API (maintenance-work-order-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Ordres de travail maintenance. Corrective, preventive et predictive. DIFFERENCE vs maintenance-schedule-api : Maintenance Work Order = OT executes, Maintenance Schedule = planification preventive.

## Endpoints
- GET /v1/work-orders : OT en cours
- POST /v1/work-orders : Creer OT
- GET /v1/work-orders/{id} : Detail OT
- PUT /v1/work-orders/{id} : Modifier
- POST /v1/work-orders/{id} : Cloturer OT
- GET /v1/work-orders/{id}/labor : Main oeuvre
- POST /v1/work-orders/{id}/labor : Declarer temps

Authentification : apiKey