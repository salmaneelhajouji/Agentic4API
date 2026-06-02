# Media Processing API (media-processing-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Pipeline de traitement multimédia. Transcodage vidéo, OCR sur images/PDF, watermarking, compression et détection de contenu. DIFFÉRENCE vs media-api : Media API gère le stockage, CDN et le resize simple d'images, Media Processing API effectue des transformations complexes (transcodage vidéo, OCR, watermark, détection IA de contenu). DIFFÉRENCE vs file-storage-api : File Storage = stockage générique, Media Processing = traitement et transformation du contenu multimédia.

## Endpoints
- POST /v1/media-processing/transcode : Transcoder une vidéo (MP4, WebM, HLS, DASH)
- POST /v1/media-processing/ocr : OCR sur image ou PDF — extraction de texte
- POST /v1/media-processing/watermark : Ajouter un watermark (texte ou logo) sur image ou vidéo
- POST /v1/media-processing/detect-content : Détection IA de contenu inapproprié (nudité, violence, NSFW)
- GET /v1/media-processing/jobs/{jobId} : Statut d'un job de traitement asynchrone

Authentification : Clé API Kong Gateway — Devoteam nexDigital