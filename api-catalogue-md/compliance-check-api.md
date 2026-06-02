# Compliance Check API (compliance-check-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Conformité réglementaire. ISO 27001, RGPD, PCI-DSS et audits.

## Endpoints
- POST /v1/compliance/check : Lancer audit conformité
- GET /v1/compliance/frameworks : Référentiels disponibles
- GET /v1/compliance/reports/{orgId} : Rapport conformité
- POST /v1/compliance/reports/{orgId} : Générer rapport
- GET /v1/compliance/gaps : Écarts identifiés
- POST /v1/compliance/gaps : Plan correction

Authentification : apiKey