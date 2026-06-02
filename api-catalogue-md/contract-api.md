# Contract API (contract-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Legal

Gestion des contrats juridiques. Rédaction, négociation, signature et suivi des échéances contractuelles. DIFFÉRENCE vs document-api : Contract API gère le cycle de vie juridique complet (négociation, versions, obligations, renouvellement), Document API génère des documents depuis des templates. DIFFÉRENCE vs invoice-api : Contract est un accord juridique entre parties, Invoice est un document fiscal de facturation.

## Endpoints
- POST /v1/contracts : Créer un contrat
- GET /v1/contracts : Lister les contrats
- GET /v1/contracts/{id} : Contrat complet avec historique de versions
- PUT /v1/contracts/{id} : Modifier le contrat (crée une nouvelle version)
- POST /v1/contracts/{id}/sign : Envoyer en signature aux parties
- GET /v1/contracts/{id}/obligations : Obligations contractuelles et échéances
- POST /v1/contracts/{id}/obligations : Ajouter une obligation (livrable, paiement, etc.)
- POST /v1/contracts/{id}/renew : Renouveler un contrat expiré ou arrivant à terme

Authentification : Clé API Kong Gateway — Devoteam nexDigital