# Broker API (broker-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Gestion courtiers et apporteurs. Commissions, mandats et portefeuilles.

## Endpoints
- GET /v1/brokers : Courtiers actifs
- POST /v1/brokers : Ajouter courtier
- GET /v1/brokers/{id} : Profile courtier
- PUT /v1/brokers/{id} : Modifier
- GET /v1/brokers/{id}/commission : Commissions
- POST /v1/brokers/{id}/commission : Calculer
- GET /v1/brokers/{id}/portfolio : Portefeuille client

Authentification : apiKey