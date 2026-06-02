# Email API (email-api)
Version v2 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Envoi d'emails transactionnels et marketing avec templates, tracking et gestion des bounces. Canal email seul. DIFFÉRENCE vs notification-api : Email API se spécialise sur l'email avec templates Handlebars, tracking ouverture/clic, listes de suppression. Notification API orchestre plusieurs canaux sans ces fonctionnalités avancées.

## Endpoints
- POST /v2/emails/send : Envoyer un email transactionnel
- POST /v2/emails/batch : Envoi en masse (max 10 000 destinataires)
- GET /v2/emails/{id}/status : Statut de livraison d'un email
- GET /v2/emails/templates : Lister les templates email
- POST /v2/emails/templates : Créer un template email (Handlebars)
- GET /v2/emails/suppressions : Lister les adresses supprimées (bounces, unsubscribes)

Authentification : Clé API Kong Gateway