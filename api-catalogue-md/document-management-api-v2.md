# Document Management API (document-management-api-v2)
Version v2 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Gestion electronique documents. Upload, versioning, recherche et workflow validation.

## Endpoints
- GET /v2/documents : Catalogue
- POST /v2/documents : Uploader
- GET /v2/documents/{id} : Detail
- PUT /v2/documents/{id} : Modifier
- DELETE /v2/documents/{id} : Archiver
- GET /v2/documents/{id}/versions : Versions
- POST /v2/documents/{id}/versions : Nouvelle version
- POST /v2/documents/{id}/workflow : Soumettre validation
- PUT /v2/documents/{id}/workflow : Approuver

Authentification : apiKey