# Referral API (referral-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe Marketing

Programme de parrainage. Codes de référence, tracking et récompenses.

## Endpoints
- POST /v1/referrals/generate : Générer un code de parrainage
- GET /v1/referrals/{code} : Détails d'un code de parrainage
- POST /v1/referrals/validate : Valider un parrainage lors d'une inscription
- GET /v1/referrals/{userId}/stats : Statistiques de parrainage d'un utilisateur

Authentification : Clé API Kong Gateway