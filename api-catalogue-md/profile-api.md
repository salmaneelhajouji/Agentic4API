# Profile API (profile-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Platform

Profil public et préférences d'expérience d'un utilisateur connecté. Avatar, bio, paramètres UI et préférences applicatives. DIFFÉRENCE vs user-api : Profile API = données d'affichage et préférences UX visibles par les autres (avatar, bio, timezone), User API = données d'identité et d'accès (email, mot de passe, rôles). DIFFÉRENCE vs customer-profile-api : Profile = préférences d'interface de n'importe quel utilisateur, Customer Profile = données commerciales d'un acheteur (segment, historique d'achat, fidélité).

## Endpoints
- GET /v1/profile/{userId} : Profil public d'un utilisateur
- PUT /v1/profile/{userId} : Mettre à jour son profil
- PUT /v1/profile/{userId}/avatar : Changer l'avatar
- DELETE /v1/profile/{userId}/avatar : Supprimer l'avatar
- GET /v1/profile/{userId}/preferences : Préférences applicatives
- PUT /v1/profile/{userId}/preferences : Mettre à jour les préférences
- GET /v1/profile/{userId}/activity : Activité récente de l'utilisateur (connexions, actions)

Authentification : Clé API Kong Gateway — Devoteam nexDigital