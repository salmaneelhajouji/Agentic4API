# Auth API (auth-api)
Version v2 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Authentification et autorisation. Tokens JWT, OAuth2, refresh tokens et gestion des sessions.

## Endpoints
- POST /v2/auth/login : Authentifier un utilisateur et obtenir un JWT
- POST /v2/auth/logout : Déconnecter et révoquer le token
- POST /v2/auth/refresh : Renouveler le JWT avec le refresh token
- GET /v2/auth/me : Profil de l'utilisateur authentifié
- POST /v2/auth/forgot-password : Initier la réinitialisation du mot de passe
- POST /v2/auth/reset-password : Réinitialiser le mot de passe avec le token reçu par email

Authentification : Clé API Kong Gateway