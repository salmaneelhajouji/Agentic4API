# Security Incident API (security-incident-api-v2)
Version v2 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Gestion incidents sécurité. Detection, triage, investigation et clôture. DIFFERENCE vs vulnerability-api : Security Incident = attaque active en cours, Vulnerability = faille passive non exploitée.

## Endpoints
- GET /v2/incidents : Incidents en cours
- POST /v2/incidents : Déclarer incident
- GET /v2/incidents/{id} : Detail
- PUT /v2/incidents/{id} : Mettre a jour
- GET /v2/incidents/{id}/timeline : Chronologie
- POST /v2/incidents/{id}/timeline : Ajouter événement
- GET /v2/incidents/{id}/response : Plan de réponse
- POST /v2/incidents/{id}/response : Exécuter action

Authentification : apiKey