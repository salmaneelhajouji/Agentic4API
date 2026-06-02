# Event Bus API (event-bus-api)
Version v1 - statut : active
Domaine : Cross
Equipe : Equipe Divers

Bus d'evenements. Publication, souscription et replay. DIFFERENCE vs streaming-api : Event Bus = evenements metier asynchrones, Streaming = flux donnees haute frequence.

## Endpoints
- POST /v1/events : Publier evenement
- GET /v1/events : Types evenements
- GET /v1/events/subscriptions : Abonnements
- POST /v1/events/subscriptions : S'abonner
- POST /v1/events/replay/{correlationId} : Rejouer evenements

Authentification : apiKey