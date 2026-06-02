# Workflow API (workflow-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Orchestration de workflows métier. Définition, exécution et suivi des processus automatisés.

## Endpoints
- POST /v1/workflows : Créer un workflow
- GET /v1/workflows : Lister les workflows
- POST /v1/workflows/{id}/start : Démarrer une instance du workflow
- GET /v1/workflows/{id}/status : Statut d'une instance
- PUT /v1/workflows/{id}/cancel : Annuler une instance en cours
- GET /v1/workflows/{id}/history : Historique des exécutions

Authentification : Clé API Kong Gateway