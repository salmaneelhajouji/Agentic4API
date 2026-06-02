# Customer Profile API (customer-profile-api-v2)
Version v2 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe CRM

Version 2 du profil client. Enrichit avec score de propension, tags comportementaux et champs RGPD explicites. DIFFÉRENCE vs v1 : ajout propensity_score, behavioral_tags, consent_status et historique des segments.

## Endpoints
- GET /v2/customers : Lister avec filtres enrichis (score, tags, consentement)
- POST /v2/customers : Créer un profil client v2
- GET /v2/customers/{id} : Profil enrichi d'un client
- PUT /v2/customers/{id} : Mettre à jour le profil
- GET /v2/customers/{id}/segment-history : Historique des changements de segment
- GET /v2/customers/{id}/propensity : Score de propension à l'achat (ML)

Authentification : Clé API Kong Gateway — contacter votre équipe platform