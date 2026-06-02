# Notification API (notification-api)
Version v1 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Orchestrateur de notifications multicanal (email, SMS, push) vers les utilisateurs finaux. DIFFÉRENCE vs email-api : Notification = façade multi-canal, Email = canal email seul avec templates. DIFFÉRENCE vs messaging-api : Notification = unidirectionnel (système→user), Messaging = bidirectionnel (user↔user). DIFFÉRENCE vs alert-api : Notification cible les clients, Alert cible les équipes ops. DIFFÉRENCE vs sms-api : Notification orchestre tous les canaux, SMS = canal SMS seul.

## Endpoints
- POST /v1/notifications/send : Envoyer une notification immédiate multicanal
- POST /v1/notifications/schedule : Planifier une notification future
- GET /v1/notifications/{id} : Statut d'une notification
- DELETE /v1/notifications/{id} : Annuler (statut pending uniquement)
- GET /v1/notifications : Lister avec filtres
- GET /v1/notifications/stats : Statistiques d'envoi par canal

Authentification : Clé API Kong Gateway