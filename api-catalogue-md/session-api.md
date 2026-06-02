# Session API (session-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Gestion des sessions actives. Liste, révocation et détection de sessions suspectes. DIFFÉRENCE vs auth-api : Session API consulte et révoque les sessions existantes, Auth API les crée.

## Endpoints
- GET /v1/sessions/{userId} : Sessions actives d'un utilisateur
- DELETE /v1/sessions/{sessionId} : Révoquer une session spécifique
- DELETE /v1/sessions/{userId}/revoke-all : Révoquer toutes les sessions (déconnexion totale)
- GET /v1/sessions/suspicious : Sessions suspectes détectées (géoloc inhabituelle, IP blacklistée)

Authentification : apiKey