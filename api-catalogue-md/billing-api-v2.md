# Billing API (billing-api-v2)
Version v2 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Version 2 de l'API facturation. Métered billing (usage-based), taxes automatiques et portail self-service. DIFFÉRENCE vs v1 : ajout facturation à l'usage, taxes auto via tax-api et portail client.

## Endpoints
- POST /v2/billing/subscriptions : Créer abonnement avec billing au usage
- POST /v2/billing/usage : Reporter la consommation (métered billing)
- POST /v2/billing/portal/{customerId} : Générer un lien vers le portail self-service client

Authentification : apiKey