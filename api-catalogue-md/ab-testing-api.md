# A/B Testing API (ab-testing-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Expérimentations et tests A/B. Variantes, assignation et analyse statistique des résultats.

## Endpoints
- POST /v1/experiments : Créer une expérience A/B
- GET /v1/experiments : Lister les expériences
- GET /v1/experiments/{id} : Détails d'une expérience
- POST /v1/experiments/{id}/assign : Assigner un utilisateur à une variante
- POST /v1/experiments/{id}/convert : Enregistrer une conversion
- GET /v1/experiments/{id}/results : Résultats statistiques de l'expérience

Authentification : Clé API Kong Gateway