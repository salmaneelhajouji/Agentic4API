# Key Rotation API (key-rotation-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Rotation clés cryptographiques. HSM, KMS et politiques rotation. DIFFERENCE vs certificate-management-api : Key Rotation = clés symétriques/asymétriques KMS, Certificate Management = certificats X.509 publics.

## Endpoints
- GET /v1/keys : Clés cryptographiques
- POST /v1/keys : Créer clé
- GET /v1/keys/{id} : Info clé
- POST /v1/keys/{id} : Rotation manuelle
- DELETE /v1/keys/{id} : Désactiver
- GET /v1/keys/rotation-policy : Politique rotation
- PUT /v1/keys/rotation-policy : Mettre a jour

Authentification : apiKey