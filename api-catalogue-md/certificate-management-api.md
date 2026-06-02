# Certificate Management API (certificate-management-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Gestion certificats SSL/TLS. Émission, renouvellement et révocation. DIFFERENCE vs key-rotation-api : Certificate Management = certificats X.509 PKI, Key Rotation = rotation clés cryptographiques.

## Endpoints
- GET /v1/certificates : Certificats actifs
- POST /v1/certificates : Émettre certificat
- GET /v1/certificates/{id} : Detail certificat
- POST /v1/certificates/{id} : Renouveler
- DELETE /v1/certificates/{id} : Révoquer
- GET /v1/certificates/expiring : Certificats expirant bientôt

Authentification : apiKey