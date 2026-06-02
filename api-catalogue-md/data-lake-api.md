# Data Lake API (data-lake-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Data lake. Zones, partitions et acces. DIFFERENCE vs data-warehouse-api : Data Lake = donnees brutes non structurees, Data Warehouse = donnees structurees agregees.

## Endpoints
- GET /v1/datalake/zones : Zones
- POST /v1/datalake/zones : Creer
- GET /v1/datalake/zones/{zone}/objects : Objets
- POST /v1/datalake/zones/{zone}/objects : Uploader
- DELETE /v1/datalake/zones/{zone}/objects : Supprimer

Authentification : apiKey