# Feature Flag API (feature-flag-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Feature flags et déploiement progressif (canary, A/B). DIFFÉRENCE vs config-api : Feature Flag = activation/désactivation de fonctionnalités avec rollout progressif et ciblage utilisateurs, Config = paramètres de configuration génériques.

## Endpoints
- GET /v1/flags : Lister les feature flags
- POST /v1/flags : Créer un feature flag
- GET /v1/flags/{key} : Valeur d'un flag pour un contexte utilisateur
- PUT /v1/flags/{key} : Mettre à jour un flag
- DELETE /v1/flags/{key} : Supprimer un flag
- PUT /v1/flags/{key}/rollout : Ajuster le pourcentage de rollout

Authentification : Clé API Kong Gateway — contacter votre équipe platform