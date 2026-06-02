# Fraud Claims API (fraud-claims-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Détection fraude sinistres. Scoring, signaux d'alerte et investigation. DIFFERENCE vs fraud-detection-api (banque) : Fraud Claims = fraude assurance/sinistres, Fraud Detection = fraude transactions bancaires.

## Endpoints
- POST /v1/fraud/claims/score : Scorer sinistre suspect
- GET /v1/fraud/claims/alerts : Alertes fraude
- PUT /v1/fraud/claims/alerts : Ouvrir investigation
- GET /v1/fraud/claims/patterns : Patterns fraude détectés

Authentification : apiKey