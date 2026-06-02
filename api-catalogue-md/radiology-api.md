# Radiology API (radiology-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Imagerie médicale (radio, scanner, IRM). Planification examens, résultats DICOM et comptes-rendus.

## Endpoints
- GET /v1/imaging/orders : Demandes imagerie
- POST /v1/imaging/orders : Prescrire examen
- GET /v1/imaging/orders/{id} : Détail examen
- PUT /v1/imaging/orders/{id} : Statut
- GET /v1/imaging/orders/{id}/results : Résultats DICOM
- POST /v1/imaging/orders/{id}/results : Compte-rendu

Authentification : apiKey