# User API (user-api-v3)
Version v3 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Version actuelle recommandée. Ajout de la gestion des identités fédérées (SSO externe), des groupes d'utilisateurs, du provisioning SCIM 2.0 et de l'audit trail complet. DIFFÉRENCE vs user-api-v2 : v3 introduit SCIM, les groupes natifs et la délégation de rôles.

## Endpoints
- POST /v3/users : Créer utilisateur avec groupes et IdP liés
- GET /v3/users : Lister avec filtres SCIM-compatibles
- GET /v3/users/{id} : Profil complet avec groupes et IdP
- PUT /v3/users/{id} : Mettre à jour
- DELETE /v3/users/{id} : Désactiver (soft delete avec audit)
- GET /v3/users/{id}/groups : Groupes d'un utilisateur
- POST /v3/users/{id}/groups : Ajouter à un groupe
- GET /v3/groups : Lister les groupes
- POST /v3/groups : Créer un groupe
- GET /v3/scim/v2/Users : Endpoint SCIM 2.0 — liste des utilisateurs (nouveau en v3)
- POST /v3/scim/v2/Users : Endpoint SCIM 2.0 — provisionner un utilisateur

Authentification : Clé API Kong Gateway — Devoteam nexDigital