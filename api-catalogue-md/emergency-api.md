# Emergency API (emergency-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Gestion des urgences médicales. Triage CCMU, passages aux urgences et orientation services.

## Endpoints
- GET /v1/emergency/triage : File de triage
- POST /v1/emergency/triage : Enregistrer triage
- GET /v1/emergency/cases : Cas en cours
- POST /v1/emergency/cases : Ouvrir cas urgence
- GET /v1/emergency/cases/{id} : Détail cas
- PUT /v1/emergency/cases/{id} : Mettre à jour
- POST /v1/emergency/cases/{id} : Clore

Authentification : apiKey