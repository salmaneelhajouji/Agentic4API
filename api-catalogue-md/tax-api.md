# Tax API (tax-api)
Version v1 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Calcul des taxes et TVA selon les régions. Conformité fiscale internationale et déclarations.

## Endpoints
- POST /v1/tax/calculate : Calculer les taxes d'une transaction
- GET /v1/tax/rates : Taux de TVA par pays
- POST /v1/tax/validate-vat : Valider un numéro de TVA intracommunautaire
- GET /v1/tax/reports : Rapport fiscal par période

Authentification : Clé API Kong Gateway