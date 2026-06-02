# Live Chat API (live-chat-api)
Version v1 - statut : active
Domaine : Customer Support
Equipe : Equipe Support

Chat en direct avec les agents de support. Sessions, transcriptions et transferts. DIFFÉRENCE vs messaging-api : Live Chat = communication client↔agent support avec files d'attente et SLA, Messaging = chat libre entre utilisateurs. DIFFÉRENCE vs ticket-api : Live Chat = interaction temps réel, Ticket = asynchrone.

## Endpoints
- POST /v1/chat/sessions : Démarrer une session de live chat
- GET /v1/chat/sessions/{id} : Statut d'une session
- POST /v1/chat/sessions/{id}/messages : Envoyer un message dans la session
- GET /v1/chat/sessions/{id}/messages : Historique de la session
- POST /v1/chat/sessions/{id}/transfer : Transférer vers un autre agent ou département
- PUT /v1/chat/sessions/{id}/close : Fermer la session et générer la transcription

Authentification : Clé API Kong Gateway — contacter votre équipe platform