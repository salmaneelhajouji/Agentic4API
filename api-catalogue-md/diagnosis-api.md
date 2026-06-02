# Diagnosis API (diagnosis-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Aide au diagnostic médical. Codification CIM-10/CIM-11, suggestions IA et arbres de décision clinique.

## Endpoints
- GET /v1/diagnoses/{patientId} : Diagnostics du patient
- POST /v1/diagnoses/{patientId} : Poser diagnostic
- POST /v1/diagnoses/suggest : Suggestion diagnostique IA
- GET /v1/diagnoses/icd/{code} : Informations code CIM-11

Authentification : apiKey