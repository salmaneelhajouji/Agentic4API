# Inventory Telecom API (inventory-telecom-api)
Version v1 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Inventaire SIM, equipements et materiel. Stock et affectation. DIFFERENCE vs inventory-api : Inventory Telecom = SIM/equipements reseau, Inventory = produits retail.

## Endpoints
- GET /v1/inventory-telecom/sim : Stock SIM
- POST /v1/inventory-telecom/sim : Ajouter SIM
- GET /v1/inventory-telecom/equipment : Equipements
- POST /v1/inventory-telecom/equipment : Affecter

Authentification : apiKey