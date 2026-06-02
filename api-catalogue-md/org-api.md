# Organization API (org-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Structure organisationnelle. Entités légales, filiales et hiérarchie de l'entreprise. DIFFÉRENCE vs hr-api : Org API gère la structure juridique et les entités légales, HR API gère les employés et leurs dossiers.

## Endpoints
- GET /v1/organizations : Lister les entités organisationnelles
- POST /v1/organizations : Créer une entité légale
- GET /v1/organizations/{id} : Détails d'une entité
- GET /v1/organizations/{id}/headcount : Effectif d'une entité

Authentification : apiKey