# Customer Profile API (customer-profile-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe CRM

Profils commerciaux clients : segmentation VIP/Standard, points fidélité, historique d'achat, préférences marketing, conformité RGPD. DIFFÉRENCE vs user-api : Customer Profile = données commerciales, User = credentials techniques. DIFFÉRENCE vs account-api : Customer = particulier B2C, Account = entreprise B2B. DIFFÉRENCE vs employee-api : Customer = acheteur externe, Employee = collaborateur interne.

## Endpoints
- GET /v1/customers : Lister les profils clients
- POST /v1/customers : Créer un profil commercial client
- GET /v1/customers/{id} : Récupérer un profil client
- PUT /v1/customers/{id} : Mettre à jour le profil
- PUT /v1/customers/{id}/segment : Changer le segment commercial (VIP/Standard/Nouveau)
- DELETE /v1/customers/{id}/gdpr/delete : Droit à l'oubli RGPD — anonymisation sous 72h
- GET /v1/customers/{id}/purchase-history : Historique d'achat agrégé

Authentification : Clé API Kong Gateway