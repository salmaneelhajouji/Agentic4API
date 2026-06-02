# File Storage API (file-storage-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Stockage de fichiers. Upload, téléchargement et organisation. DIFFÉRENCE vs media-api : File Storage = tous types de fichiers (docs, données), Media API = images/vidéos avec traitement (resize, CDN).

## Endpoints
- POST /v1/files/upload : Uploader un fichier
- GET /v1/files/{id} : Métadonnées d'un fichier
- DELETE /v1/files/{id} : Supprimer un fichier
- GET /v1/files/{id}/download : Télécharger un fichier
- POST /v1/files/presigned-url : Générer une URL pré-signée (upload direct S3)

Authentification : Clé API Kong Gateway