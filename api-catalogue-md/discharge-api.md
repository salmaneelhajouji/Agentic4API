# Discharge API (discharge-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Sortie du patient. Document de sortie, ordonnances de sortie et transmission médecin traitant.

## Endpoints
- POST /v1/discharge/{patientId} : Initier sortie
- GET /v1/discharge/{patientId} : Statut
- GET /v1/discharge/{patientId}/document : Document PDF
- POST /v1/discharge/{patientId}/document : Générer
- GET /v1/discharge/{patientId}/prescriptions : Ordonnances sortie

Authentification : apiKey