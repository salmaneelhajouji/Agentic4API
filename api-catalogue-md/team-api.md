# Team API (team-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Équipes de travail transverses et fonctionnelles. Création, membres et canaux de communication d'équipe. DIFFÉRENCE vs hr-api : Team API gère les équipes de travail fonctionnelles (equipe projet, squad produit), HR API gère les dossiers administratifs RH et la structure hiérarchique. DIFFÉRENCE vs account-api : Team = équipe interne de collaborateurs, Account = organisation cliente externe B2B. DIFFÉRENCE vs org-api : Team = équipe de travail opérationnelle, Org = entité juridique de l'entreprise.

## Endpoints
- POST /v1/teams : Créer une équipe
- GET /v1/teams : Lister les équipes
- GET /v1/teams/{id} : Équipe avec membres et KPIs
- PUT /v1/teams/{id} : Mettre à jour l'équipe
- DELETE /v1/teams/{id} : Dissoudre une équipe
- GET /v1/teams/{id}/members : Membres de l'équipe
- POST /v1/teams/{id}/members : Ajouter un membre
- DELETE /v1/teams/{id}/members/{userId} : Retirer un membre
- GET /v1/teams/{id}/metrics : KPIs de l'équipe (vélocité, tâches complétées, OKRs)

Authentification : Clé API Kong Gateway — Devoteam nexDigital