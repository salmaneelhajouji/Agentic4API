# VoIP API (voip-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Telephonie sur IP. Appels, conferences et enregistrements.

## Endpoints
- GET /v1/voip/calls : Historique
- POST /v1/voip/calls : Initier appel
- GET /v1/voip/calls/{id} : Statut
- DELETE /v1/voip/calls/{id} : Raccrocher
- GET /v1/voip/conferences : Conferences
- POST /v1/voip/conferences : Creer
- GET /v1/voip/conferences/{id}/participants : Participants
- POST /v1/voip/conferences/{id}/participants : Ajouter

Authentification : apiKey