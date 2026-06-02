# Tenant API (tenant-api-v2)
Version v2 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Gestion locataires. Dossiers, scoring et suivi. DIFFERENCE vs customer-profile-api : Tenant = locataire immobilier (dossier location, garants), Customer Profile = client commercial générique.

## Endpoints
- GET /v2/tenants : Lister locataires
- POST /v2/tenants : Créer dossier
- GET /v2/tenants/{id} : Dossier locataire
- PUT /v2/tenants/{id} : Modifier
- GET /v2/tenants/{id}/scoring : Score solvabilite
- GET /v2/tenants/{id}/guarantors : Garants
- POST /v2/tenants/{id}/guarantors : Ajouter garant

Authentification : apiKey