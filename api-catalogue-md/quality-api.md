# Quality Control API (quality-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Supply

Contrôle qualité des produits reçus. Inspections, non-conformités et réclamations fournisseurs.

## Endpoints
- POST /v1/quality/inspections : Créer un rapport d'inspection
- GET /v1/quality/inspections : Lister les inspections
- GET /v1/quality/non-conformities : Non-conformités en cours
- POST /v1/quality/non-conformities : Déclarer une non-conformité

Authentification : apiKey