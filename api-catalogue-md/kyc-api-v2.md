# KYC API (kyc-api-v2)
Version v2 - statut : active
Domaine : Banking
Equipe : Equipe Banque

Verification identite KYC/AML avec biometrie et scoring LCB-FT. DIFFERENCE vs aml-api : KYC = verification identite onboarding, AML = surveillance continue transactions.

## Endpoints
- GET /v2/kyc/{clientId} : Statut KYC
- POST /v2/kyc/{clientId} : Initier
- PUT /v2/kyc/{clientId} : Mettre a jour
- POST /v2/kyc/{clientId}/documents : Soumettre document
- POST /v2/kyc/{clientId}/biometric : Soumettre biometrie

Authentification : apiKey