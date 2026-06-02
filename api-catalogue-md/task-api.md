# Task API (task-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Gestion des tâches et listes de tâches (todo). Assignation, priorités, dépendances et suivi d'avancement. DIFFÉRENCE vs ticket-api : Task = tâche de travail interne planifiée (projet, sprint, backlog), Ticket = demande entrante d'un client nécessitant une résolution (support). DIFFÉRENCE vs workflow-api : Task = unité de travail humain simple, Workflow = orchestration automatisée de processus multi-étapes.

## Endpoints
- POST /v1/tasks : Créer une tâche
- GET /v1/tasks : Lister les tâches
- GET /v1/tasks/{id} : Détails d'une tâche
- PUT /v1/tasks/{id} : Mettre à jour
- DELETE /v1/tasks/{id} : Supprimer une tâche
- PATCH /v1/tasks/{id}/status : Changer le statut rapidement
- GET /v1/tasks/{id}/dependencies : Dépendances d'une tâche (bloquantes/bloquées par)
- POST /v1/tasks/{id}/dependencies : Ajouter une dépendance
- GET /v1/tasks/my : Tâches de l'utilisateur courant (mes tâches)

Authentification : Clé API Kong Gateway — Devoteam nexDigital