# Referral Health API (referral-health-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Orientations entre professionnels de santé. Consultations spécialisées et lettres de liaison. DIFFÉRENCE vs referral-api (e-commerce) : Referral Health = orientation médicale, Referral = parrainage client.

## Endpoints
- GET /v1/referrals : Demandes orientation
- POST /v1/referrals : Créer orientation
- GET /v1/referrals/{id} : Détail
- PUT /v1/referrals/{id} : Statut
- GET /v1/referrals/{id}/letter : Lettre de liaison
- POST /v1/referrals/{id}/letter : Générer

Authentification : apiKey