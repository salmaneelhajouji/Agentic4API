# Accessibility API (accessibility-api)
Version v1 - statut : active
Domaine : Infrastructure
Equipe : Equipe Platform

Accessibilité numérique. Analyse WCAG, génération de descriptions alt-text et vérification de contrastes.

## Endpoints
- POST /v1/accessibility/analyze : Analyser l'accessibilité d'une page web
- POST /v1/accessibility/alt-text : Générer du texte alternatif pour une image (IA)
- POST /v1/accessibility/contrast : Vérifier le ratio de contraste couleur (WCAG)

Authentification : apiKey