# Housekeeping API (housekeeping-api)
Version v1 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Gestion ménage hôtelier. Planning, priorités et statut chambres.

## Endpoints
- GET /v1/housekeeping/{hotelId} : Plan ménage
- POST /v1/housekeeping/{hotelId} : Créer tâche
- GET /v1/housekeeping/rooms/{roomId} : Statut chambre
- PUT /v1/housekeeping/rooms/{roomId} : Changer statut
- GET /v1/housekeeping/staff : Equipe ménage

Authentification : apiKey