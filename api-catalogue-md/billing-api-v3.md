# Billing API (billing-api-v3)
Version v3 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Version actuelle recommandée. Ajout de la facturation hybride (flat + usage), du portail client self-service complet, de la gestion des crédits et avoirs automatiques, et de l'intégration ERP native. DIFFÉRENCE vs invoice-api : Billing orchestre les cycles de paiement récurrents, Invoice génère les documents fiscaux légaux.

## Endpoints
- POST /v3/billing/subscriptions : Créer abonnement hybride (flat + usage) avec workflow de relance
- GET /v3/billing/subscriptions : Lister les abonnements
- GET /v3/billing/subscriptions/{id} : Abonnement complet avec crédits et historique
- PUT /v3/billing/subscriptions/{id} : Modifier l'abonnement (upgrade/downgrade proratisé)
- DELETE /v3/billing/subscriptions/{id} : Résilier avec période de grâce
- POST /v3/billing/usage : Reporter consommation (métered billing)
- POST /v3/billing/credits : Émettre un crédit sur un abonnement (nouveau en v3)
- POST /v3/billing/erp-sync/{subscriptionId} : Forcer synchronisation ERP (SAP/Oracle/Sage — nouveau en v3)

Authentification : Clé API Kong Gateway — Devoteam nexDigital