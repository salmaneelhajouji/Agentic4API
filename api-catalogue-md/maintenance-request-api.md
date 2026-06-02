# Maintenance Request API (maintenance-request-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Demandes d'intervention locataires. Tickets maintenance, priorités et suivi.

## Endpoints
- GET /v1/maintenance-requests : Lister demandes
- POST /v1/maintenance-requests : Créer demande
- GET /v1/maintenance-requests/{id} : Detail
- PUT /v1/maintenance-requests/{id} : Mettre a jour statut
- POST /v1/maintenance-requests/{id} : Affecter technicien

Authentification : apiKey