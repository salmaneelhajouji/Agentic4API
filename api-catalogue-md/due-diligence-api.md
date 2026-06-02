# Due Diligence API (due-diligence-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Due diligence juridique et financiere. Checklist, documents et rapport final.

## Endpoints
- GET /v1/due-diligence : Audits en cours
- POST /v1/due-diligence : Lancer due diligence
- GET /v1/due-diligence/{id} : Avancement
- PUT /v1/due-diligence/{id} : Mettre a jour
- GET /v1/due-diligence/{id}/findings : Findings
- POST /v1/due-diligence/{id}/findings : Ajouter
- GET /v1/due-diligence/{id}/report : Rapport final

Authentification : apiKey