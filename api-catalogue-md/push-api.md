# Push Notification API (push-api)
Version v1 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Notifications push mobiles iOS et Android. Tokens, segments et campagnes push. DIFFÉRENCE vs notification-api : Push API = canal mobile seul avec gestion device tokens et segments. Notification API = façade multi-canal. DIFFÉRENCE vs messaging-api : Push = unidirectionnel système→mobile, Messaging = bidirectionnel.

## Endpoints
- POST /v1/push/send : Envoyer une notification push
- POST /v1/push/register-device : Enregistrer un device mobile
- DELETE /v1/push/unregister-device : Désenregistrer un device
- POST /v1/push/campaigns : Créer une campagne push
- GET /v1/push/campaigns/{id}/stats : Statistiques d'une campagne push

Authentification : Clé API Kong Gateway