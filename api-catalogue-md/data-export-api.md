# Data Export API (data-export-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Export massif de données en CSV, JSON ou Parquet. Jobs asynchrones et téléchargements sécurisés.

## Endpoints
- POST /v1/exports : Créer un job d'export
- GET /v1/exports/{jobId}/status : Statut du job d'export
- GET /v1/exports/{jobId}/download : Télécharger le fichier d'export (lien valable 24h)
- DELETE /v1/exports/{jobId} : Annuler un job d'export

Authentification : Clé API Kong Gateway