# Endpoint Protection API (endpoint-protection-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Protection endpoints. EDR, antivirus et gestion des postes.

## Endpoints
- GET /v1/endpoints : Endpoints managés
- POST /v1/endpoints : Enrôler endpoint
- GET /v1/endpoints/{id} : Statut protection
- POST /v1/endpoints/{id} : Isoler endpoint
- GET /v1/endpoints/{id}/threats : Menaces détectées
- POST /v1/endpoints/{id}/threats : Mettre en quarantaine

Authentification : apiKey