# Privileged Access API (privileged-access-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Gestion accès privilégiés PAM. Coffre-fort mots de passe, sessions et enregistrement.

## Endpoints
- GET /v1/pam/credentials : Comptes privilégiés
- POST /v1/pam/credentials : Ajouter
- GET /v1/pam/credentials/{id} : Emprunter credential
- POST /v1/pam/credentials/{id} : Remettre
- GET /v1/pam/sessions : Sessions privilégiées
- POST /v1/pam/sessions : Démarrer session
- GET /v1/pam/recordings : Enregistrements

Authentification : apiKey