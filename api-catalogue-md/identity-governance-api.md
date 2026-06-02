# Identity Governance API (identity-governance-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Gouvernance des identités. Cycle de vie, rôles et séparation des tâches. DIFFERENCE vs permission-api : Identity Governance = gouvernance cycle de vie identités, Permission = contrôle accès RBAC.

## Endpoints
- GET /v1/identity/governance : Statut gouvernance
- GET /v1/identity/roles : Rôles
- POST /v1/identity/roles : Créer rôle
- GET /v1/identity/sod : Règles séparation tâches
- POST /v1/identity/sod : Vérifier conflit
- GET /v1/identity/lifecycle : Cycle de vie
- POST /v1/identity/lifecycle : Provisionner

Authentification : apiKey