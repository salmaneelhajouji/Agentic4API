# Performance API (performance-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Évaluations de performance. OKRs, feedback 360° et plans de développement.

## Endpoints
- POST /v1/performance/reviews : Créer une évaluation de performance
- GET /v1/performance/{employeeId} : Historique des évaluations
- POST /v1/performance/objectives : Créer un objectif (OKR)
- PUT /v1/performance/objectives/{id}/progress : Mettre à jour la progression d'un objectif

Authentification : Clé API Kong Gateway