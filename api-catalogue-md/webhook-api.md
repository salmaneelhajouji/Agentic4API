# Webhook API (webhook-api)
Version v1 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Enregistrement et gestion des webhooks entrants/sortants. Réception d'événements externes et diffusion d'événements internes vers des endpoints configurés. Validation des signatures HMAC.

## Endpoints
- POST /v1/webhooks : Enregistrer un endpoint webhook
- GET /v1/webhooks : Lister les webhooks
- GET /v1/webhooks/{id} : Détails d'un webhook
- PUT /v1/webhooks/{id} : Mettre à jour un webhook
- DELETE /v1/webhooks/{id} : Supprimer un webhook
- POST /v1/webhooks/{id}/test : Envoyer un événement de test
- GET /v1/webhooks/{id}/deliveries : Historique des livraisons

Authentification : Clé API Kong Gateway