# Merger Acquisition API (merger-acquisition-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Fusions et acquisitions. Data room, closing et integration.

## Endpoints
- GET /v1/ma/deals : Operations M&A
- POST /v1/ma/deals : Ouvrir operation
- GET /v1/ma/deals/{id} : Detail operation
- PUT /v1/ma/deals/{id} : Mettre a jour
- GET /v1/ma/deals/{id}/dataroom : Accès data room
- POST /v1/ma/deals/{id}/dataroom : Uploader document
- GET /v1/ma/deals/{id}/milestones : Jalons closing

Authentification : apiKey