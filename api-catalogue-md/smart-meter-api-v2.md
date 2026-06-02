# Smart Meter API (smart-meter-api-v2)
Version v2 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Compteurs intelligents eau/gaz/electricite avec relevé temps réel et alertes. DIFFERENCE vs water-meter-api : Smart Meter = multi-fluides, Water Meter = eau uniquement.

## Endpoints
- GET /v2/meters : Lister compteurs
- POST /v2/meters : Enregistrer
- GET /v2/meters/{id} : Releve temps reel
- GET /v2/meters/{id}/history : Historique consommation
- GET /v2/meters/{id}/alerts : Alertes
- POST /v2/meters/{id}/alerts : Configurer seuil

Authentification : apiKey