# Compliance Legal API (compliance-legal-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Conformite reglementaire juridique. Obligations, veille et reporting. DIFFERENCE vs compliance-check-api : Compliance Legal = conformite droit des affaires, Compliance Check = conformite securite informatique.

## Endpoints
- GET /v1/compliance/legal/obligations : Obligations legales
- POST /v1/compliance/legal/obligations : Ajouter
- GET /v1/compliance/legal/{obligationId}/status : Statut conformite
- PUT /v1/compliance/legal/{obligationId}/status : Mettre a jour
- GET /v1/compliance/legal/reports : Rapports
- POST /v1/compliance/legal/reports : Générer rapport

Authentification : apiKey