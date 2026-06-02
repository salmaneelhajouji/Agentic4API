# E-Signature API (esignature-api)
Version v1 - statut : active
Domaine : Legal
Equipe : Equipe Legal

Signature electronique qualifiee eIDAS. Workflows multi-signataires et archivage probatoire.

## Endpoints
- GET /v1/esign/documents : Documents a signer
- POST /v1/esign/documents : Preparer signature
- GET /v1/esign/documents/{id} : Detail
- POST /v1/esign/documents/{id} : Envoyer
- GET /v1/esign/documents/{id}/signers : Statut signatures
- POST /v1/esign/documents/{id}/signers : Ajouter signataire
- POST /v1/esign/documents/{id}/archive : Archiver

Authentification : apiKey