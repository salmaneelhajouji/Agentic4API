# Visa API (visa-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Formalités visa et entrée pays. Vérification exigences et suivi demande.

## Endpoints
- POST /v1/visa/requirements : Vérifier exigences visa
- GET /v1/visa/applications : Demandes
- POST /v1/visa/applications : Soumettre demande
- GET /v1/visa/applications/{id} : Statut demande
- PUT /v1/visa/applications/{id} : Mettre a jour

Authentification : apiKey