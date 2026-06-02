# Logistics Tracking API (logistics-tracking-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Logistique

Tracking unifié multi-transporteurs. Agrégation des statuts de tous les transporteurs en une seule API.

## Endpoints
- GET /v1/tracking/{code} : Suivi d'un colis par numéro de tracking
- POST /v1/tracking/batch : Suivi de plusieurs colis simultanément
- GET /v1/tracking/{code}/events : Historique complet des événements de livraison

Authentification : Clé API Kong Gateway — contacter votre équipe platform