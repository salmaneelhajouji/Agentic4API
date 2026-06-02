# Smart Lock API (smart-lock-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Serrures connectées. Accès, codes temporaires et historique.

## Endpoints
- GET /v1/locks : Lister serrures
- POST /v1/locks : Enregistrer
- GET /v1/locks/{id} : Statut serrure
- POST /v1/locks/{id} : Fermer
- GET /v1/locks/{id}/access-codes : Codes d'accès
- POST /v1/locks/{id}/access-codes : Générer code temporaire
- DELETE /v1/locks/{id}/access-codes : Révoquer

Authentification : apiKey