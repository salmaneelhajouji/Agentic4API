# Notary API (notary-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Actes notaries. Ventes immobilières, successions et authentification.

## Endpoints
- GET /v1/notary/acts : Actes en cours
- POST /v1/notary/acts : Créer acte
- GET /v1/notary/acts/{id} : Detail acte
- PUT /v1/notary/acts/{id} : Modifier
- POST /v1/notary/acts/{id} : Authentifier
- GET /v1/notary/acts/{id}/parties : Parties
- POST /v1/notary/acts/{id}/parties : Ajouter partie
- POST /v1/notary/acts/{id}/archive : Archiver au rang des minutes

Authentification : apiKey