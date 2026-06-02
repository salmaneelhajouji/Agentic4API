# BOM API (bom-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Bill of Materials nomenclatures. Multi-niveaux, variantes et gestion modifications.

## Endpoints
- GET /v1/bom/{productId} : Nomenclature
- POST /v1/bom/{productId} : Creer nomenclature
- GET /v1/bom/{productId}/components : Composants
- POST /v1/bom/{productId}/components : Ajouter composant
- DELETE /v1/bom/{productId}/components : Retirer
- GET /v1/bom/{productId}/versions : Versions nomenclature
- POST /v1/bom/{productId}/versions : Publier version

Authentification : apiKey