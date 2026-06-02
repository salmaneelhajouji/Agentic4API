# Subscriber API (subscriber-api-v3)
Version v3 - statut : active
Domaine : Telecom
Equipe : Equipe Telecom

Gestion abonnes telecom. Lignes, forfaits, portabilite et cycle de vie. DIFFERENCE vs customer-profile-api : Subscriber = abonne telecom avec lignes/SIM, Customer Profile = client commercial generique.

## Endpoints
- GET /v3/subscribers : Abonnes
- POST /v3/subscribers : Creer
- GET /v3/subscribers/{id} : Profil
- PUT /v3/subscribers/{id} : Modifier
- DELETE /v3/subscribers/{id} : Resilier
- GET /v3/subscribers/{id}/lines : Lignes
- POST /v3/subscribers/{id}/lines : Ajouter
- POST /v3/subscribers/{id}/portability : Porter
- GET /v3/subscribers/{id}/portability : Statut

Authentification : apiKey