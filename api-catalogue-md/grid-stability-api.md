# Grid Stability API (grid-stability-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Stabilité et équilibrage du réseau électrique. Fréquence, tension et prédictions. DIFFERENCE vs grid-api : Grid Stability = analyse stabilité et prédictions, Grid = gestion noeuds et incidents.

## Endpoints
- GET /v1/stability/status : Statut stabilité réseau
- GET /v1/stability/frequency : Historique fréquence
- GET /v1/stability/forecast : Prévisions stabilité

Authentification : apiKey