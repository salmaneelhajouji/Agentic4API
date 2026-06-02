# Translation API (translation-api)
Version v1 - statut : active
Domaine : Localisation
Equipe : Equipe Platform

Traduction automatique de contenu. API de traduction NMT (Neural Machine Translation) pour textes et documents. DIFFÉRENCE vs localization-api : Translation API = traduction de texte brut via NMT, Localization API = gestion des clés de traduction i18n et des formats culturels.

## Endpoints
- POST /v1/translate : Traduire un texte
- POST /v1/translate/batch : Traduire plusieurs textes en une requête
- GET /v1/translate/languages : Langues supportées
- POST /v1/translate/detect : Détecter la langue d'un texte

Authentification : apiKey