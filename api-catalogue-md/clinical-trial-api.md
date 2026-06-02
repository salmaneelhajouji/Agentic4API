# Clinical Trial API (clinical-trial-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Essais cliniques. Protocoles, recrutement patients, suivi cohortes et rapports réglementaires EMA/FDA.

## Endpoints
- GET /v1/trials : Essais en cours
- POST /v1/trials : Créer protocole
- GET /v1/trials/{id} : Protocole complet
- PUT /v1/trials/{id} : Modifier
- POST /v1/trials/{id}/enroll : Inscrire patient
- GET /v1/trials/{id}/enroll : Participants

Authentification : apiKey