# Geolocation API (geolocation-api)
Version v1 - statut : active
Domaine : Localisation
Equipe : Equipe Platform

Géolocalisation et cartographie. Geocodage, distances et zones de livraison. DIFFÉRENCE vs localization-api : Geolocation = coordonnées et cartes, Localization = traductions et formats culturels.

## Endpoints
- POST /v1/geo/geocode : Convertir une adresse en coordonnées
- POST /v1/geo/reverse-geocode : Convertir des coordonnées en adresse
- POST /v1/geo/distance : Calculer la distance entre deux points
- POST /v1/geo/delivery-zone : Vérifier si une adresse est dans une zone de livraison

Authentification : Clé API Kong Gateway