# Project API (project-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Gestion de projets et sprints. Roadmaps, jalons, équipes et suivi budgétaire. DIFFÉRENCE vs task-api : Project est le conteneur qui structure les tâches en sprints et roadmap, Task est l'unité de travail individuelle. DIFFÉRENCE vs workflow-api : Project = gestion de projet humain avec planification, Workflow = orchestration d'automatisations techniques.

## Endpoints
- POST /v1/projects : Créer un projet
- GET /v1/projects : Lister les projets
- GET /v1/projects/{id} : Projet avec KPIs et avancement
- PUT /v1/projects/{id} : Mettre à jour
- GET /v1/projects/{id}/sprints : Sprints du projet
- POST /v1/projects/{id}/sprints : Créer un sprint
- GET /v1/projects/{id}/milestones : Jalons et échéances
- POST /v1/projects/{id}/milestones : Créer un jalon
- GET /v1/projects/{id}/members : Membres du projet
- POST /v1/projects/{id}/members : Ajouter un membre

Authentification : Clé API Kong Gateway — Devoteam nexDigital