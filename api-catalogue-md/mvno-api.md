# MVNO API (mvno-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Operateurs virtuels MVNO. Accords, decomptes et marges.

## Endpoints
- GET /v1/mvno/partners : MVNO
- POST /v1/mvno/partners : Ajouter
- GET /v1/mvno/partners/{id} : Detail
- PUT /v1/mvno/partners/{id} : Modifier
- GET /v1/mvno/partners/{id}/settlement : Decompte
- POST /v1/mvno/partners/{id}/settlement : Generer

Authentification : apiKey