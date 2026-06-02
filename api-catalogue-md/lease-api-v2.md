# Lease API (lease-api-v2)
Version v2 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Contrats de bail résidentiels et commerciaux. Indexation, révision et résiliation. DIFFERENCE vs property-api : Lease = contrat juridique de location, Property = bien immobilier.

## Endpoints
- GET /v2/leases : Lister baux
- POST /v2/leases : Créer bail
- GET /v2/leases/{id} : Detail bail
- PUT /v2/leases/{id} : Modifier
- DELETE /v2/leases/{id} : Résilier
- GET /v2/leases/{id}/indexation : Calcul indexation
- POST /v2/leases/{id}/indexation : Appliquer révision
- GET /v2/leases/{id}/documents : Documents bail

Authentification : apiKey