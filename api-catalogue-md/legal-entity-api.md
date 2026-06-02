# Legal Entity API (legal-entity-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Gestion entites juridiques. Societes, associations et etablissements. DIFFERENCE vs company-profile-api : Legal Entity = donnees juridiques officielles SIREN/SIRET, Company Profile = profil commercial.

## Endpoints
- GET /v1/entities : Entites
- POST /v1/entities : Créer entite
- GET /v1/entities/{id} : Detail entite
- PUT /v1/entities/{id} : Modifier
- GET /v1/entities/{id}/documents : Documents officiels
- POST /v1/entities/{id}/documents : Ajouter
- POST /v1/entities/search : Rechercher par SIREN/SIRET

Authentification : apiKey