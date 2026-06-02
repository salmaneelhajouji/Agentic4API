# Maintenance Schedule API (maintenance-schedule-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Planification maintenance préventive véhicules. Kilométrage, temps et alertes.

## Endpoints
- GET /v1/schedule/{vehicleId} : Planning maintenance
- POST /v1/schedule/{vehicleId} : Ajouter tache
- GET /v1/schedule/{vehicleId}/upcoming : Maintenances a venir
- GET /v1/schedule/alerts : Alertes maintenance

Authentification : apiKey