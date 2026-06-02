# SOC API (soc-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Security Operations Center. Gestion des analystes, tickets et escalades.

## Endpoints
- GET /v1/soc/tickets : Tickets en cours
- POST /v1/soc/tickets : Créer ticket
- GET /v1/soc/tickets/{id} : Detail
- PUT /v1/soc/tickets/{id} : Mettre a jour
- POST /v1/soc/tickets/{id} : Escalader
- GET /v1/soc/analysts : Analystes disponibles
- POST /v1/soc/analysts : Assigner
- GET /v1/soc/metrics : KPIs SOC

Authentification : apiKey