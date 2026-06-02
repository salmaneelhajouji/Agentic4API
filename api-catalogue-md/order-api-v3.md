# Order API (order-api-v3)
Version v3 - statut : deprecated
Domaine : E-Commerce
Equipe : Equipe Commerce

Version 3 — DEPRECATED sept. 2023. Adresse structurée, statut partially_shipped, objet discount enrichi.

## Endpoints
- POST /v3/orders : Créer une commande avec adresse structurée
- GET /v3/orders : Lister avec filtres avancés
- GET /v3/orders/{id} : Récupérer une commande
- PUT /v3/orders/{id} : Modifier (avant expédition)
- PUT /v3/orders/{id}/cancel : Annuler avec option remboursement
- POST /v3/orders/{id}/ship : Expédier tout ou partie — BREAKING v4: supprimé, utiliser PATCH /status

Authentification : Clé API Kong Gateway