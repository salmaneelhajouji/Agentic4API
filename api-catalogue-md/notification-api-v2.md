# Notification API (notification-api-v2)
Version v2 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Version 2 de la Notification API. Ajout des templates multilingues, des préférences utilisateur par canal et du retry automatique. DIFFÉRENCE vs v1 : templates versionnés, opt-out par canal, batching asynchrone.

## Endpoints
- POST /v2/notifications/send : Envoyer via template ou message brut, multi-canal
- POST /v2/notifications/batch : Envoi groupé asynchrone (max 50 000 destinataires)
- GET /v2/notifications/{id} : Statut et logs de livraison
- DELETE /v2/notifications/{id} : Annuler si pending
- GET /v2/notifications/preferences/{userId} : Préférences de notification d'un utilisateur
- PUT /v2/notifications/preferences/{userId} : Mettre à jour les préférences (opt-out par canal)
- GET /v2/notifications/templates : Lister les templates de notification
- POST /v2/notifications/templates : Créer un template multilingue

Authentification : Clé API Kong Gateway — contacter votre équipe platform