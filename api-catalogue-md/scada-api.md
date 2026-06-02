# SCADA API (scada-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

SCADA supervision industrielle. Acquisition donnees terrain et telecommande.

## Endpoints
- GET /v1/scada/tags : Tags SCADA
- POST /v1/scada/tags : Ajouter tag
- GET /v1/scada/tags/{id} : Valeur temps reel
- PUT /v1/scada/tags/{id} : Ecrire valeur
- GET /v1/scada/alarms : Alarmes actives
- PUT /v1/scada/alarms : Effacer
- POST /v1/scada/historian : Interroger historique

Authentification : apiKey