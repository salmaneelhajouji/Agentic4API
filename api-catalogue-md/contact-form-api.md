# Contact Form API (contact-form-api)
Version v1 - statut : active
Domaine : Customer Support
Equipe : Equipe Support

Formulaires de contact web et mobile. Réception, routing et conversion en tickets. DIFFÉRENCE vs ticket-api : Contact Form = point d'entrée côté client (formulaire), Ticket API = gestion interne des demandes (backoffice).

## Endpoints
- POST /v1/contact/submit : Soumettre un formulaire de contact
- GET /v1/contact/forms : Lister les formulaires configurés
- POST /v1/contact/forms : Créer un formulaire de contact

Authentification : Clé API Kong Gateway — contacter votre équipe platform