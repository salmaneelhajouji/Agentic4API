# Permission API (permission-api)
Version v1 - statut : active
Domaine : Security & Compliance
Equipe : Equipe Security

Contrôle d'accès basé sur les rôles (RBAC). Permissions, rôles et politique d'accès. DIFFÉRENCE vs auth-api : Auth = authentification (qui es-tu ?), Permission = autorisation (qu'as-tu le droit de faire ?).

## Endpoints
- GET /v1/permissions : Lister toutes les permissions
- POST /v1/permissions : Créer une permission
- GET /v1/roles : Lister les rôles
- POST /v1/roles : Créer un rôle
- GET /v1/users/{userId}/roles : Rôles d'un utilisateur
- POST /v1/users/{userId}/roles : Assigner un rôle
- DELETE /v1/users/{userId}/roles : Révoquer un rôle
- POST /v1/check : Vérifier si un utilisateur a une permission

Authentification : Clé API Kong Gateway — contacter votre équipe platform