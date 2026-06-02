# Escrow Real Estate API (escrow-real-estate-api)
Version v1 - statut : active
Domaine : RealEstate
Equipe : Equipe Immobilier

Séquestre immobilier. Consignation des fonds, conditions et libération. DIFFERENCE vs escrow-api (e-commerce) : Escrow Real Estate = séquestre transactions immobilières, Escrow = séquestre e-commerce.

## Endpoints
- GET /v1/escrow/real-estate : Séquestres en cours
- POST /v1/escrow/real-estate : Créer séquestre
- GET /v1/escrow/real-estate/{id} : Detail séquestre
- POST /v1/escrow/real-estate/{id} : Annuler

Authentification : apiKey