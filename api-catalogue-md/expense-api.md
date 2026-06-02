# Expense API (expense-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe Finance

Notes de frais et remboursements employés. Soumission, validation et virement.

## Endpoints
- POST /v1/expenses : Soumettre une note de frais
- GET /v1/expenses : Lister les notes de frais
- GET /v1/expenses/{id} : Détails d'une note de frais
- PUT /v1/expenses/{id}/approve : Approuver
- PUT /v1/expenses/{id}/reject : Rejeter

Authentification : Clé API Kong Gateway — contacter votre équipe platform