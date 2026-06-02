# Data Loss Prevention API (data-loss-prevention-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Prévention fuite de données. Détection, blocage et alertes DLP.

## Endpoints
- GET /v1/dlp/policies : Politiques DLP
- POST /v1/dlp/policies : Créer politique
- GET /v1/dlp/incidents : Incidents DLP
- POST /v1/dlp/incidents : Signaler
- GET /v1/dlp/incidents/{id} : Detail
- PUT /v1/dlp/incidents/{id} : Résoudre
- POST /v1/dlp/scan : Scanner données

Authentification : apiKey