# SSO API (sso-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Identity

Single Sign-On SAML 2.0 et OpenID Connect. Fédération d'identité avec les IdP externes (Azure AD, Okta, Google). DIFFÉRENCE vs auth-api : SSO = fédération vers IdP externes, Auth = authentification locale JWT.

## Endpoints
- GET /v1/sso/providers : Lister les IdP configurés
- POST /v1/sso/providers : Configurer un IdP SSO
- GET /v1/sso/login/{providerId} : Initier le flux SSO (redirection vers IdP)
- POST /v1/sso/callback : Callback SSO (assertion SAML ou code OIDC)

Authentification : apiKey