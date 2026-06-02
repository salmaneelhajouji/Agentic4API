# Notification API (notification-api-v3)
Version v3 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Version actuelle. Ajout des canaux WhatsApp et in-app, du système de règles de déclenchement (triggers), de la personnalisation IA et du rate-limiting par utilisateur. DIFFÉRENCE vs notification-api-v2 : v3 ajoute WhatsApp, les triggers événementiels et la personnalisation IA des contenus.

## Endpoints
- POST /v3/notifications/send : Envoyer (email/SMS/push/WhatsApp/in-app) avec personnalisation IA
- POST /v3/notifications/triggers : Créer une règle de déclenchement événementielle (nouveau en v3)
- GET /v3/notifications/triggers : Lister les règles de déclenchement
- GET /v3/notifications/in-app/{userId} : Notifications in-app non lues d'un utilisateur (nouveau canal v3)
- PATCH /v3/notifications/in-app/{userId} : Marquer en lues
- GET /v3/notifications/{id} : Statut et logs de livraison
- DELETE /v3/notifications/{id} : Annuler si pending

Authentification : Clé API Kong Gateway — Devoteam nexDigital