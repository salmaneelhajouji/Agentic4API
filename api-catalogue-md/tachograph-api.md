# Tachograph API (tachograph-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Tachygraphe numérique. Temps de conduite, repos et conformité réglementaire.

## Endpoints
- GET /v1/tachograph/{driverId} : Données tachygraphe
- POST /v1/tachograph/{driverId} : Importer données
- GET /v1/tachograph/{driverId}/compliance : Infractions
- GET /v1/tachograph/{driverId}/rest-periods : Périodes de repos

Authentification : apiKey