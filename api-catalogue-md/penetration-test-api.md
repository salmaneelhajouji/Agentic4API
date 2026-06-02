# Penetration Test API (penetration-test-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Tests d'intrusion. Planification, exécution et rapports.

## Endpoints
- GET /v1/pentests : Tests planifiés
- POST /v1/pentests : Créer test
- GET /v1/pentests/{id} : Detail
- PUT /v1/pentests/{id} : Modifier
- POST /v1/pentests/{id} : Lancer
- GET /v1/pentests/{id}/findings : Résultats
- POST /v1/pentests/{id}/findings : Ajouter finding
- GET /v1/pentests/{id}/report : Rapport final

Authentification : apiKey