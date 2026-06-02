# Cargo API (cargo-api-v2)
Version v2 - statut : active
Domaine : Transport
Equipe : Equipe Transport

Gestion fret et marchandises. Chargement, manifestes et suivi. DIFFERENCE vs shipping-api : Cargo = fret lourd/industriel (conteneurs, vrac), Shipping = colis e-commerce.

## Endpoints
- GET /v2/cargo : Lister cargaisons
- POST /v2/cargo : Créer cargaison
- GET /v2/cargo/{id} : Detail
- PUT /v2/cargo/{id} : Modifier
- GET /v2/cargo/{id}/manifest : Manifeste
- POST /v2/cargo/{id}/manifest : Générer
- GET /v2/cargo/{id}/customs : Documents douane

Authentification : apiKey