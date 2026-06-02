# Queue API (queue-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Files d'attente de messages asynchrones. Publication, consommation et gestion des dead-letter queues.

## Endpoints
- GET /v1/queues : Lister les queues
- POST /v1/queues : Créer une queue
- POST /v1/queues/{name}/publish : Publier un message
- GET /v1/queues/{name}/consume : Consommer des messages (max 10)
- DELETE /v1/queues/{name}/messages/{id}/ack : Acquitter un message (le supprime de la queue)
- GET /v1/queues/{name}/dlq : Messages en dead-letter queue (échecs après max_retries)

Authentification : Clé API Kong Gateway — contacter votre équipe platform