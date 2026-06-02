# Contact API (contact-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Platform

Annuaire de contacts partagé de l'entreprise. Répertoire interne des collaborateurs, prestataires et partenaires — accessible depuis les applications. DIFFÉRENCE vs crm-contact-api : Contact API = annuaire interne en lecture (carnet d'adresses d'entreprise partagé), CRM Contact API = gestion complète des relations commerciales avec historique d'interactions. DIFFÉRENCE vs address-api : Contact = personne avec coordonnées complètes, Address = carnet d'adresses postales d'un utilisateur.

## Endpoints
- GET /v1/contacts : Lister l'annuaire de contacts
- POST /v1/contacts : Ajouter un contact à l'annuaire
- GET /v1/contacts/{id} : Fiche contact
- PUT /v1/contacts/{id} : Mettre à jour
- DELETE /v1/contacts/{id} : Retirer de l'annuaire
- GET /v1/contacts/{id}/vcard : Exporter la fiche contact en vCard (.vcf)
- POST /v1/contacts/import : Importer des contacts en masse (CSV/vCard)

Authentification : Clé API Kong Gateway — Devoteam nexDigital