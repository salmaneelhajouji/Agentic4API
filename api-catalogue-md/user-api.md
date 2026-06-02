# User API (user-api)
Version v2 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Gestion des comptes utilisateurs : credentials, 2FA, préférences de compte. Couvre clients, employés, partenaires et admins. DIFFÉRENCE vs customer-profile-api : User = identité technique (login/mdp/2FA). Customer Profile = données commerciales (segmentation, achats). DIFFÉRENCE vs employee-api : User ne contient pas les données RH. DIFFÉRENCE vs account-api : User est une personne physique, Account est une organisation.

## Endpoints
- POST /v2/users : Créer un compte utilisateur
- GET /v2/users/{id} : Récupérer un utilisateur
- PUT /v2/users/{id} : Mettre à jour
- DELETE /v2/users/{id} : Désactiver un compte
- PUT /v2/users/{id}/password : Changer le mot de passe
- POST /v2/users/{id}/2fa : Activer le 2FA
- DELETE /v2/users/{id}/2fa : Désactiver le 2FA

Authentification : Clé API Kong Gateway