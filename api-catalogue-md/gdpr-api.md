# GDPR API (gdpr-api)
Version v1 - statut : active
Domaine : Security & Compliance
Equipe : Equipe Security

Conformité RGPD. Droit à l'oubli, portabilité des données et gestion des consentements.

## Endpoints
- POST /v1/gdpr/delete-request : Demande de suppression (droit à l'oubli)
- POST /v1/gdpr/export-request : Demande de portabilité des données
- GET /v1/gdpr/consents/{userId} : Consentements d'un utilisateur
- PUT /v1/gdpr/consents/{userId} : Mettre à jour les consentements
- GET /v1/gdpr/requests/{id}/status : Statut d'une demande RGPD

Authentification : Clé API Kong Gateway