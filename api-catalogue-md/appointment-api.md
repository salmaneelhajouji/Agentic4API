# Appointment API (appointment-api)
Version v1 - statut : active
Domaine : Customer Support
Equipe : Equipe Support

Prise de rendez-vous clients. Réservation de créneaux avec des conseillers ou techniciens. DIFFÉRENCE vs delivery-api : Appointment = RDV avec une personne (conseiller, technicien), Delivery = créneau de livraison de colis. DIFFÉRENCE vs calendar-api : Appointment gère les réservations côté client, Calendar gère les disponibilités internes.

## Endpoints
- POST /v1/appointments : Prendre un rendez-vous
- GET /v1/appointments : Lister les rendez-vous
- GET /v1/appointments/{id} : Détails d'un rendez-vous
- PUT /v1/appointments/{id} : Reporter un rendez-vous
- DELETE /v1/appointments/{id} : Annuler un rendez-vous
- GET /v1/appointments/slots : Créneaux disponibles

Authentification : Clé API Kong Gateway — contacter votre équipe platform