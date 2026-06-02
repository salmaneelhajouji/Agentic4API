# Load Planning API (load-planning-api)
Version v1 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Planification chargement véhicules. Optimisation espace, poids et contraintes.

## Endpoints
- GET /v1/loads : Chargements planifiés
- POST /v1/loads : Créer plan chargement
- GET /v1/loads/{id} : Plan chargement
- PUT /v1/loads/{id} : Modifier
- POST /v1/loads/optimize : Optimiser chargement

Authentification : apiKey