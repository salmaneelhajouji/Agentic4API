# eSIM API (esim-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Gestion eSIM. Profils, activation et transfert.

## Endpoints
- GET /v1/esim/{deviceId} : Profils
- POST /v1/esim/{deviceId} : Activer
- POST /v1/esim/{deviceId}/transfer : Transferer
- GET /v1/esim/qrcode/{profileId} : QR code

Authentification : apiKey