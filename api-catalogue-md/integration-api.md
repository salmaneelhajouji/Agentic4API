# Integration API (integration-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Connecteurs vers systèmes tiers. ERP, CRM externes, marketplaces et plateformes partenaires.

## Endpoints
- GET /v1/integrations : Lister les intégrations disponibles
- POST /v1/integrations/{name}/connect : Connecter une intégration
- DELETE /v1/integrations/{name}/disconnect : Déconnecter une intégration
- POST /v1/integrations/{name}/sync : Forcer une synchronisation
- GET /v1/integrations/{name}/status : Statut de connexion

Authentification : Clé API Kong Gateway