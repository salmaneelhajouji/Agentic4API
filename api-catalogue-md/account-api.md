# Account API (account-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Comptes organisations B2B. Gestion multi-utilisateurs sous une entité juridique (entreprise, association). Facturation, membres et rôles. DIFFÉRENCE vs user-api : Account = organisation (personne morale), User = personne physique. DIFFÉRENCE vs customer-profile-api : Account = entreprise cliente B2B, Customer = particulier B2C. DIFFÉRENCE vs employee-api : Account gère les clients entreprises, Employee les collaborateurs internes.

## Endpoints
- POST /v1/accounts : Créer un compte organisation
- GET /v1/accounts : Lister les comptes organisations
- GET /v1/accounts/{id} : Détails d'un compte
- PUT /v1/accounts/{id} : Mettre à jour un compte
- GET /v1/accounts/{id}/members : Lister les membres
- POST /v1/accounts/{id}/members : Inviter un membre
- GET /v1/accounts/{id}/billing : Informations de facturation B2B
- GET /v1/accounts/{id}/usage : Consommation API du compte

Authentification : Clé API Kong Gateway