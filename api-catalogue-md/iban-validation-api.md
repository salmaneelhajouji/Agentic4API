# IBAN Validation API (iban-validation-api)
Version v1 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Validation IBAN/BIC. DIFFERENCE vs transfer-api : IBAN Validation = verification avant operation, Transfer = execution virement.

## Endpoints
- POST /v1/iban/validate : Valider IBAN
- GET /v1/iban/decode/{iban} : Decoder IBAN

Authentification : apiKey