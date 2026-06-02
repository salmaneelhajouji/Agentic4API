# Threat Intelligence API (threat-intelligence-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Renseignement sur les menaces. IoC, acteurs malveillants et TTPs.

## Endpoints
- GET /v1/threats : Menaces actives
- POST /v1/threats : Ajouter menace
- GET /v1/threats/{id} : Detail menace
- POST /v1/threats/ioc/check : Ingérer IoC
- GET /v1/threats/feeds : Flux renseignement
- POST /v1/threats/feeds : S'abonner
- GET /v1/threats/actors : Acteurs malveillants

Authentification : apiKey