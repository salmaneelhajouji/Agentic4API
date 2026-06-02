# Store Locator API (store-locator-api)
Version v1 - statut : active
Domaine : Localisation
Equipe : Equipe Commerce

Points de vente et magasins. Recherche par proximité, horaires et stocks en magasin.

## Endpoints
- GET /v1/stores/nearby : Magasins proches d'une position
- GET /v1/stores/{id} : Détails d'un magasin
- GET /v1/stores/{id}/hours : Horaires d'ouverture
- GET /v1/stores/{id}/stock/{productId} : Disponibilité d'un produit en magasin

Authentification : Clé API Kong Gateway