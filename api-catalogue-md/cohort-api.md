# Cohort API (cohort-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Analyse de cohortes clients. Rétention, LTV et comportement par groupe d'acquisition.

## Endpoints
- POST /v1/cohorts : Créer une analyse de cohorte
- GET /v1/cohorts : Lister les cohortes
- GET /v1/cohorts/{id}/retention : Matrice de rétention
- GET /v1/cohorts/{id}/ltv : LTV de la cohorte par période

Authentification : Clé API Kong Gateway — contacter votre équipe platform