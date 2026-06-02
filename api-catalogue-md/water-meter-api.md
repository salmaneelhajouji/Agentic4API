# Water Meter API (water-meter-api)
Version v1 - statut : active
Domaine : IoT
Equipe : Equipe IoT

Compteurs eau intelligents. Consommation, fuites et facturation. DIFFERENCE vs smart-meter-api : Water Meter = eau uniquement avec detection fuites, Smart Meter = multi-fluides generique.

## Endpoints
- GET /v1/water-meters : Lister
- POST /v1/water-meters : Enregistrer
- GET /v1/water-meters/{id} : Releve eau
- GET /v1/water-meters/{id}/leak-detection : Detecter fuites

Authentification : apiKey