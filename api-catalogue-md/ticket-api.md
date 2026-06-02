# Ticket API (ticket-api)
Version v1 - statut : active
Domaine : Customer Support
Equipe : Equipe Support

Tickets de support client. Création, assignation, escalade et résolution des incidents.

## Endpoints
- POST /v1/tickets : Créer un ticket support
- GET /v1/tickets : Lister les tickets
- GET /v1/tickets/{id} : Détails d'un ticket
- PUT /v1/tickets/{id}/assign : Assigner à un agent
- PUT /v1/tickets/{id}/escalate : Escalader un ticket
- PUT /v1/tickets/{id}/close : Fermer un ticket
- POST /v1/tickets/{id}/comments : Ajouter un commentaire au ticket

Authentification : Clé API Kong Gateway