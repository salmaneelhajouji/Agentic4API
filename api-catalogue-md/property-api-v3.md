# Property API (property-api-v3)
Version v3 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Biens immobiliers complets. Diagnostics DPE, photos 3D et valorisation IA. DIFFERENCE vs lease-api : Property = bien immobilier, Lease = contrat de bail sur ce bien.

## Endpoints
- GET /v3/properties : Lister biens
- POST /v3/properties : Créer bien
- GET /v3/properties/{id} : Detail complet
- PUT /v3/properties/{id} : Modifier
- DELETE /v3/properties/{id} : Supprimer
- GET /v3/properties/{id}/valuation : Valorisation IA
- GET /v3/properties/{id}/diagnostics : DPE et diagnostics
- POST /v3/properties/{id}/diagnostics : Ajouter
- GET /v3/properties/{id}/photos : Photos
- POST /v3/properties/{id}/photos : Ajouter photo

Authentification : apiKey