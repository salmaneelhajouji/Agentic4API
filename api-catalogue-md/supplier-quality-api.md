# Supplier Quality API (supplier-quality-api)
Version v1 - statut : active
Domaine : Industry
Equipe : Equipe Industrie

Qualite fournisseurs. Evaluation, audits et non-conformites. DIFFERENCE vs quality-control-api : Supplier Quality = qualite entrants fournisseurs, Quality Control = qualite production interne.

## Endpoints
- GET /v1/supplier-quality/{supplierId} : Score qualite fournisseur
- GET /v1/supplier-quality/audits : Audits fournisseurs
- POST /v1/supplier-quality/audits : Creer audit
- GET /v1/supplier-quality/ncs : NC fournisseurs
- POST /v1/supplier-quality/ncs : Declarer NC

Authentification : apiKey