# Segmentation API (segmentation-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe CRM

Segmentation dynamique des clients. Règles comportementales et attributs pour ciblage.

## Endpoints
- POST /v1/segments : Créer un segment
- GET /v1/segments : Lister les segments
- GET /v1/segments/{id}/members : Membres d'un segment
- PUT /v1/segments/{id}/rules : Mettre à jour les règles de segmentation
- POST /v1/segments/preview : Prévisualiser un segment avant création

Authentification : Clé API Kong Gateway