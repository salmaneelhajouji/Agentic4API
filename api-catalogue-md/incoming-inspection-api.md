# Incoming Inspection API (incoming-inspection-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Reception et controle entrants. Controle a reception, echantillonnage et acceptation.

## Endpoints
- GET /v1/incoming/{poId} : Controle reception
- POST /v1/incoming/{poId} : Enregistrer
- GET /v1/incoming/{poId}/sampling : Plan echantillonnage
- POST /v1/incoming/{poId}/sampling : Resultat

Authentification : apiKey