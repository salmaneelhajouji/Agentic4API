# User API (user-api-v1)
Version v1 - statut : deprecated
Domaine : Identity & Access
Equipe : Equipe Identity

Version 1 de l'API utilisateurs. DEPRECATED 2022. Pas de 2FA, rôles simples (admin/user), pas de statut suspendu. Migrer vers v2.

## Endpoints
- POST /v1/users : Créer un utilisateur (sans 2FA)
- GET /v1/users : Lister les utilisateurs
- GET /v1/users/{id} : Profil utilisateur
- PUT /v1/users/{id} : Mettre à jour
- DELETE /v1/users/{id} : Supprimer définitivement (BREAKING v2: soft delete)

Authentification : Clé API Kong Gateway — contacter votre équipe platform