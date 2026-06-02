# Campaign API (campaign-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe Marketing

Campagnes marketing multicanal. Création, segmentation, planification et analyse des performances.

## Endpoints
- POST /v1/campaigns : Créer une campagne
- GET /v1/campaigns : Lister les campagnes
- GET /v1/campaigns/{id} : Détails d'une campagne
- PUT /v1/campaigns/{id}/launch : Lancer une campagne
- PUT /v1/campaigns/{id}/pause : Mettre en pause
- GET /v1/campaigns/{id}/stats : Performances de la campagne

Authentification : Clé API Kong Gateway