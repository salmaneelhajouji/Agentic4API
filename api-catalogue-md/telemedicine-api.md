# Telemedicine API (telemedicine-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Téléconsultation médicale. Planification visio-consultations, salle d'attente virtuelle et compte-rendu.

## Endpoints
- GET /v1/teleconsult : Consultations planifiées
- POST /v1/teleconsult : Planifier
- GET /v1/teleconsult/{id} : Détail
- DELETE /v1/teleconsult/{id} : Annuler
- POST /v1/teleconsult/{id}/start : Démarrer session vidéo
- POST /v1/teleconsult/{id}/summary : Ajouter compte-rendu

Authentification : apiKey