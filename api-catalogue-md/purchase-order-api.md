# Purchase Order API (purchase-order-api)
Version v1 - statut : active
Domaine : Supply Chain
Equipe : Equipe Supply

Bons de commande fournisseurs. Gestion des achats, réceptions et rapprochements. DIFFÉRENCE vs order-api : Purchase Order = commandes passées AUX fournisseurs (B2B achats), Order API = commandes passées PAR les clients (B2C ventes).

## Endpoints
- POST /v1/purchase-orders : Créer un bon de commande fournisseur
- GET /v1/purchase-orders : Lister les bons de commande
- GET /v1/purchase-orders/{id} : Détails d'un bon de commande
- POST /v1/purchase-orders/{id}/receive : Enregistrer une réception de marchandises

Authentification : Clé API Kong Gateway — contacter votre équipe platform