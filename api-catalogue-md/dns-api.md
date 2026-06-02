# DNS API (dns-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Gestion des enregistrements DNS. A, CNAME, MX et TTL.

## Endpoints
- GET /v1/dns/zones : Lister les zones DNS
- POST /v1/dns/zones : Créer une zone DNS
- GET /v1/dns/zones/{zone}/records : Enregistrements d'une zone
- POST /v1/dns/zones/{zone}/records : Ajouter un enregistrement DNS
- PUT /v1/dns/zones/{zone}/records/{id} : Modifier un enregistrement
- DELETE /v1/dns/zones/{zone}/records/{id} : Supprimer un enregistrement

Authentification : Clé API Kong Gateway — contacter votre équipe platform