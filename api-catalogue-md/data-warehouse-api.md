# Data Warehouse API (data-warehouse-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Entrepot donnees structure. Tables, vues et requetes BI. DIFFERENCE vs data-lake-api : Data Warehouse = donnees structurees pour BI, Data Lake = donnees brutes.

## Endpoints
- GET /v1/warehouse/schemas : Schemas
- POST /v1/warehouse/schemas : Creer
- GET /v1/warehouse/tables/{schema} : Tables
- POST /v1/warehouse/tables/{schema} : Creer
- POST /v1/warehouse/query : Executer SQL
- GET /v1/warehouse/query : Historique

Authentification : apiKey