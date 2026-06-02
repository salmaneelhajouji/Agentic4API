# Escrow API (escrow-api)
Version v1 - statut : active
Domaine : Finance
Equipe : Equipe Finance

Paiements sous séquestre pour marketplaces. Fonds retenus jusqu'à confirmation de livraison, puis libérés.

## Endpoints
- POST /v1/escrow : Créer un compte séquestre
- GET /v1/escrow/{id} : Statut du séquestre
- POST /v1/escrow/{id}/release : Libérer les fonds vers le vendeur
- POST /v1/escrow/{id}/refund : Rembourser l'acheteur (litige)

Authentification : apiKey