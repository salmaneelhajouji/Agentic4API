# Renovation API (renovation-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Gestion travaux de rénovation. Devis, planning et suivi chantier.

## Endpoints
- GET /v1/renovations : Projets en cours
- POST /v1/renovations : Créer projet
- GET /v1/renovations/{id} : Detail projet
- PUT /v1/renovations/{id} : Modifier
- GET /v1/renovations/{id}/quotes : Devis
- POST /v1/renovations/{id}/quotes : Ajouter devis
- GET /v1/renovations/{id}/progress : Avancement
- POST /v1/renovations/{id}/progress : Mettre a jour

Authentification : apiKey