# Document API (document-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Génération de documents (contrats, CGV, devis). Templates Word/PDF et signature électronique. DIFFÉRENCE vs file-storage-api : Document API génère des documents à partir de templates, File Storage stocke des fichiers existants.

## Endpoints
- POST /v1/documents/generate : Générer un document depuis un template
- GET /v1/documents/templates : Lister les templates disponibles
- POST /v1/documents/templates : Créer un template document
- POST /v1/documents/{id}/sign : Demander une signature électronique

Authentification : apiKey