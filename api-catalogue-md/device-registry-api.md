# Device Registry API (device-registry-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Registre des appareils IoT. Enregistrement, provisioning et gestion du cycle de vie.

## Endpoints
- GET /v1/devices : Lister appareils
- POST /v1/devices : Enregistrer appareil
- GET /v1/devices/{id} : Detail
- PUT /v1/devices/{id} : Modifier
- DELETE /v1/devices/{id} : Désactiver
- GET /v1/devices/{id}/firmware : Version firmware
- POST /v1/devices/{id}/firmware : Mise a jour

Authentification : apiKey