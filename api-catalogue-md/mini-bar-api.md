# Mini Bar API (mini-bar-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Gestion mini-bars hôteliers. Consommations, réapprovisionnement et facturation.

## Endpoints
- GET /v1/minibar/{roomId} : Articles mini-bar
- POST /v1/minibar/{roomId} : Enregistrer consommation
- PUT /v1/minibar/{roomId} : Réapprovisionner
- GET /v1/minibar/{bookingId}/bill : Facture consommations

Authentification : apiKey