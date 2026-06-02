# Auth API (auth-api-v1)
Version v1 - statut : deprecated
Domaine : Identity & Access
Equipe : Equipe Identity

Version 1 de l'Auth API. DEPRECATED 2022. Sessions serveur sans JWT, pas de refresh token, pas d'OAuth2. Migrer vers v2 (JWT stateless).

## Endpoints
- POST /v1/auth/login : Connexion par session serveur (cookies)
- POST /v1/auth/logout : Déconnexion (invalidation session serveur)
- GET /v1/auth/me : Profil depuis session

Authentification : Clé API Kong Gateway — contacter votre équipe platform