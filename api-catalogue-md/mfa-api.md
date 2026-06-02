# MFA API (mfa-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Authentification multi-facteurs. TOTP, SMS, et clés hardware (FIDO2/WebAuthn). DIFFÉRENCE vs user-api : MFA API gère tous les facteurs d'authentification (pas seulement le 2FA Google), User API gère l'identité. DIFFÉRENCE vs sms-api : MFA SMS passe par MFA API pour l'OTP d'authentification.

## Endpoints
- POST /v1/mfa/enroll : Enrôler un nouveau facteur MFA
- POST /v1/mfa/verify : Vérifier un facteur MFA
- GET /v1/mfa/{userId}/factors : Facteurs MFA actifs d'un utilisateur
- DELETE /v1/mfa/{userId}/factors/{factorId} : Révoquer un facteur MFA

Authentification : apiKey