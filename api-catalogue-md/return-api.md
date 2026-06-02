# Return API (return-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Commerce

Retours produits et remboursements. Demandes, validation, suivi et logistique inverse.

## Endpoints
- POST /v1/returns : Créer une demande de retour
- GET /v1/returns/{id} : Statut d'une demande de retour
- PUT /v1/returns/{id}/approve : Approuver le retour
- PUT /v1/returns/{id}/reject : Rejeter la demande de retour
- GET /v1/returns?orderId={id} : Retours d'une commande

Authentification : Clé API Kong Gateway