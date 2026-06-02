# Subscription API (subscription-api)
Version v2 - statut : active
Domaine : E-Commerce
Equipe : Equipe Commerce

Abonnements produits et services. Plans, upgrades et résiliations. DIFFÉRENCE vs billing-api : Subscription = plan et droits d'accès, Billing = paiements récurrents.

## Endpoints
- GET /v2/subscriptions/{customerId} : Abonnements actifs d'un client
- POST /v2/subscriptions : Souscrire à un plan
- PUT /v2/subscriptions/{id}/upgrade : Upgrader vers un plan supérieur
- PUT /v2/subscriptions/{id}/downgrade : Downgrader vers un plan inférieur
- DELETE /v2/subscriptions/{id} : Résilier l'abonnement

Authentification : Clé API Kong Gateway