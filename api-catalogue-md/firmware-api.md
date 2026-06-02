# Firmware API (firmware-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Gestion des mises a jour firmware OTA. Distribution, déploiement progressif et rollback. DIFFERENCE vs device-registry-api : Firmware = MAJ logicielle, Device Registry = inventaire materiel.

## Endpoints
- GET /v1/firmware/releases : Releases disponibles
- POST /v1/firmware/releases : Publier release
- GET /v1/firmware/releases/{id} : Detail release
- GET /v1/firmware/deployments : Déploiements en cours
- POST /v1/firmware/deployments : Lancer déploiement
- GET /v1/firmware/deployments/{id} : Statut
- DELETE /v1/firmware/deployments/{id} : Rollback

Authentification : apiKey