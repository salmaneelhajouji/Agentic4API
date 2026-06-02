# Data Processing Agreement API (data-processing-agreement-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Accords de traitement de donnees RGPD. DPA sous-traitants et gestion consentements. DIFFERENCE vs gdpr-api : DPA = contrat entre responsable et sous-traitant, GDPR = droits des personnes concernees.

## Endpoints
- GET /v1/dpa : DPA en vigueur
- POST /v1/dpa : Créer DPA
- GET /v1/dpa/{id} : Detail DPA
- PUT /v1/dpa/{id} : Modifier
- POST /v1/dpa/{id} : Signer
- GET /v1/dpa/{id}/processors : Sous-traitants
- POST /v1/dpa/{id}/processors : Ajouter

Authentification : apiKey