# Lab Result API (lab-result-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Résultats d'analyses biologiques et de laboratoire. DIFFÉRENCE vs vital-signs-api : Lab = analyses biologiques ponctuelles, Vital Signs = constantes physiologiques continues.

## Endpoints
- GET /v1/results/{patientId} : Résultats analyses
- POST /v1/results/{patientId} : Ajouter résultat
- GET /v1/results/{patientId}/critical : Valeurs critiques

Authentification : apiKey