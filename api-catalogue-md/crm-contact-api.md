# CRM Contact API (crm-contact-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe CRM

Contacts CRM : clients, prospects et partenaires. Segmentation, enrichissement et historique d'interactions. DIFFÉRENCE vs customer-profile-api : CRM Contact = vue 360° toutes relations (prospects, partenaires), Customer Profile = uniquement les acheteurs B2C.

## Endpoints
- POST /v1/crm/contacts : Créer un contact CRM
- GET /v1/crm/contacts : Lister les contacts
- GET /v1/crm/contacts/{id} : Fiche contact
- PUT /v1/crm/contacts/{id} : Mettre à jour
- DELETE /v1/crm/contacts/{id} : Supprimer un contact
- POST /v1/crm/contacts/search : Recherche avancée de contacts
- GET /v1/crm/contacts/{id}/interactions : Historique des interactions
- POST /v1/crm/contacts/{id}/interactions : Ajouter une interaction (appel, email, réunion)

Authentification : Clé API Kong Gateway