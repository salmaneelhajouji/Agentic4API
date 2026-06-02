# Secret Manager API (secret-api)
Version v1 - statut : active
Domaine : Security & Compliance
Equipe : Equipe Security

Gestionnaire de secrets. Credentials, tokens et certificats stockés de manière sécurisée. DIFFÉRENCE vs api-key-api : Secret Manager = stockage générique de tous types de secrets (mots de passe, certificats, tokens tiers), API Key API = gestion spécifique des clés d'accès à nos APIs.

## Endpoints
- POST /v1/secrets : Créer un secret
- GET /v1/secrets : Lister les secrets (métadonnées uniquement)
- GET /v1/secrets/{name} : Lire la valeur d'un secret
- PUT /v1/secrets/{name} : Mettre à jour la valeur
- DELETE /v1/secrets/{name} : Supprimer un secret
- GET /v1/secrets/{name}/versions : Historique des versions d'un secret

Authentification : Clé API Kong Gateway — contacter votre équipe platform