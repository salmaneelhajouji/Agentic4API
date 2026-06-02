# Encryption API (encryption-api)
Version v1 - statut : active
Domaine : Security & Compliance
Equipe : Equipe Security

Chiffrement et gestion des clés cryptographiques. AES, RSA et gestion de vault.

## Endpoints
- POST /v1/encrypt : Chiffrer une donnée
- POST /v1/decrypt : Déchiffrer une donnée
- POST /v1/keys : Générer une clé cryptographique
- GET /v1/keys : Lister les clés (métadonnées uniquement)
- POST /v1/keys/{id}/rotate : Rotation d'une clé cryptographique

Authentification : Clé API Kong Gateway — contacter votre équipe platform