# Allergy API (allergy-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Registre allergies et intolérances médicamenteuses et alimentaires. Alertes automatiques à la prescription.

## Endpoints
- GET /v1/allergies/{patientId} : Allergies du patient
- POST /v1/allergies/{patientId} : Déclarer allergie
- DELETE /v1/allergies/{patientId} : Supprimer
- GET /v1/allergies/{patientId}/check/{drugId} : Vérifier risque allergique

Authentification : apiKey