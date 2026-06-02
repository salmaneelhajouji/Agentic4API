# AML Legal API (aml-legal-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Lutte anti-blanchiment obligations professions juridiques. Declarations TRACFIN avocats/notaires. DIFFERENCE vs aml-api banque : AML Legal = obligations LCB-FT professions juridiques, AML = monitoring transactions bancaires.

## Endpoints
- POST /v1/aml-legal/screening : Cribler transaction
- GET /v1/aml-legal/declarations : Declarations TRACFIN
- POST /v1/aml-legal/declarations : Declarer au TRACFIN
- GET /v1/aml-legal/risk/{clientId} : Niveau risque client

Authentification : apiKey