# Supplier API (supplier-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Supply

Fournisseurs et partenaires B2B. Catalogue, contrats et évaluations.

## Endpoints
- POST /v1/suppliers : Créer un fournisseur
- GET /v1/suppliers : Lister les fournisseurs
- GET /v1/suppliers/{id} : Fiche fournisseur
- PUT /v1/suppliers/{id} : Mettre à jour
- GET /v1/suppliers/{id}/products : Catalogue du fournisseur
- POST /v1/suppliers/{id}/evaluate : Évaluer un fournisseur

Authentification : Clé API Kong Gateway