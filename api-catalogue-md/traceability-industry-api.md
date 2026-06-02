# Traceability Industry API (traceability-industry-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Tracabilite produits industriels. Numeros serie, lots et historique. DIFFERENCE vs traceability-agri-api : Traceability Industry = tracabilite pieces et lots industriels, Traceability Agri = traçabilite produits agricoles.

## Endpoints
- GET /v1/traceability/{serialNumber} : Arbre composants
- GET /v1/traceability/lots/{lotId} : Expedition lot

Authentification : apiKey