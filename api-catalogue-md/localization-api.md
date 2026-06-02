# Localization API (localization-api)
Version v1 - statut : active
Domaine : Localisation
Equipe : Equipe Platform

Traductions et internationalisation. Langues, devises et formats régionaux. DIFFÉRENCE vs geolocation-api : Localization = textes et formats culturels (i18n), Geolocation = coordonnées GPS.

## Endpoints
- GET /v1/l10n/translations/{lang} : Toutes les traductions d'une langue
- GET /v1/l10n/currencies : Devises supportées avec taux de change
- POST /v1/l10n/translate : Traduire un texte dynamiquement
- GET /v1/l10n/formats/{country} : Formats régionaux (date, nombre, monnaie)

Authentification : Clé API Kong Gateway