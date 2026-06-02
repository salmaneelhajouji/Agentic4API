# Media API (media-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Médias images et vidéos. Upload, redimensionnement, optimisation et CDN. DIFFÉRENCE vs file-storage-api : Media = traitement multimédia (resize, compress, CDN), File Storage = stockage générique sans traitement.

## Endpoints
- POST /v1/media/upload : Uploader un média (image ou vidéo)
- GET /v1/media/{id} : Métadonnées d'un média
- DELETE /v1/media/{id} : Supprimer un média
- POST /v1/media/{id}/resize : Redimensionner une image
- GET /v1/media/{id}/cdn-url : URL CDN optimisée d'un média

Authentification : Clé API Kong Gateway