# Onboarding API (onboarding-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Parcours d'intégration des nouveaux employés. Checklist, documents et accès à provisionner.

## Endpoints
- POST /v1/onboarding/start : Démarrer le parcours d'onboarding
- GET /v1/onboarding/{employeeId} : Statut du parcours d'onboarding
- PUT /v1/onboarding/{employeeId}/tasks/{taskId}/complete : Marquer une tâche d'onboarding comme complétée
- POST /v1/onboarding/{employeeId}/provision-access : Provisionner automatiquement les accès systèmes

Authentification : apiKey