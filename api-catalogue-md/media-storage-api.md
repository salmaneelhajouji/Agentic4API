# Media Storage API (media-storage-api)
Version v1 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Stockage medias. Upload, CDN et transformation images. DIFFERENCE vs document-management-api : Media Storage = fichiers binaires medias CDN, Document Management = GED documents metier.

## Endpoints
- POST /v1/media/upload : Uploader media
- GET /v1/media/{id} : Info media
- DELETE /v1/media/{id} : Supprimer
- POST /v1/media/{id}/transform : Transformer image
- GET /v1/media/{id}/transform : Media transforme
- GET /v1/media/folders : Dossiers
- POST /v1/media/folders : Creer

Authentification : apiKey