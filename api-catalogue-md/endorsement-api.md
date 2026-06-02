# Endorsement API (endorsement-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Avenants et modifications de contrats. Ajout garanties, changement données. DIFFERENCE vs policy-api : Endorsement = modification ponctuelle d'un contrat existant, Policy = gestion contrat complet.

## Endpoints
- GET /v1/endorsements : Avenants en cours
- POST /v1/endorsements : Créer avenant
- GET /v1/endorsements/{id} : Detail avenant
- POST /v1/endorsements/{id} : Approuver
- DELETE /v1/endorsements/{id} : Annuler

Authentification : apiKey