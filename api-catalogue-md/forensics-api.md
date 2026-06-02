# Forensics API (forensics-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Investigation numérique forensique. Analyse artefacts, mémoire et disques.

## Endpoints
- GET /v1/forensics/cases : Dossiers forensique
- POST /v1/forensics/cases : Ouvrir dossier
- GET /v1/forensics/cases/{id} : Detail dossier
- PUT /v1/forensics/cases/{id} : Mettre a jour
- GET /v1/forensics/cases/{id}/artifacts : Artefacts collectés
- POST /v1/forensics/cases/{id}/artifacts : Ajouter artefact
- GET /v1/forensics/cases/{id}/report : Rapport forensique

Authentification : apiKey