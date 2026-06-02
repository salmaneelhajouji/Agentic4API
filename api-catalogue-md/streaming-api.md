# Streaming API (streaming-api)
Version v1 - statut : active
Domaine : Data
Equipe : Equipe Data

Traitement temps reel. Topics, consumers et offsets.

## Endpoints
- GET /v1/streaming/topics : Topics
- POST /v1/streaming/topics : Creer
- DELETE /v1/streaming/topics : Supprimer
- POST /v1/streaming/topics/{topic}/produce : Produire
- GET /v1/streaming/topics/{topic}/consume : Consommer
- GET /v1/streaming/consumers : Consumers
- POST /v1/streaming/consumers : Creer

Authentification : apiKey