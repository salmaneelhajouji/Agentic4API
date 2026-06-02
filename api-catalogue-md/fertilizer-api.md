# Fertilizer API (fertilizer-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Gestion fertilisants et intrants. Stocks, applications et bilan azoté.

## Endpoints
- GET /v1/fertilizers : Fertilisants disponibles
- POST /v1/fertilizers : Ajouter produit
- GET /v1/fertilizers/{fieldId}/application : Applications
- POST /v1/fertilizers/{fieldId}/application : Enregistrer application
- GET /v1/fertilizers/{fieldId}/balance : Bilan azoté

Authentification : apiKey