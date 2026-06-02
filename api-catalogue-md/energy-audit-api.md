# Energy Audit API (energy-audit-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Audits énergétiques bâtiments. DPE, recommandations et suivi travaux. DIFFERENCE vs carbon-footprint-api : Energy Audit = diagnostic bâtiment DPE, Carbon Footprint = bilan carbone activités.

## Endpoints
- GET /v1/audits : Audits réalisés
- POST /v1/audits : Commander audit
- GET /v1/audits/{id} : Rapport DPE
- PUT /v1/audits/{id} : Modifier
- GET /v1/audits/{id}/recommendations : Recommandations travaux

Authentification : apiKey