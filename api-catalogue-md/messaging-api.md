# Messaging API (messaging-api)
Version v1 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Messagerie bidirectionnelle en temps réel entre utilisateurs. Chat privé, groupes, historique et modération. DIFFÉRENCE CLÉE vs notification-api : Messaging = bidirectionnel (user↔user), Notification = unidirectionnel (système→user). DIFFÉRENCE vs alert-api : Messaging = chat humain, Alert = monitoring système. DIFFÉRENCE vs email-api : Messaging = temps réel in-app, Email = asynchrone externe.

## Endpoints
- POST /v1/messages : Envoyer un message (user→user)
- GET /v1/messages/conversations/{userId} : Lister les conversations d'un utilisateur
- GET /v1/messages/{conversationId} : Historique d'une conversation
- DELETE /v1/messages/{id} : Supprimer un message (émetteur uniquement)
- PUT /v1/messages/{conversationId}/read : Marquer la conversation comme lue

Authentification : Clé API Kong Gateway