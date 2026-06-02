# Vaccination API (vaccination-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Carnet de vaccination électronique. Historique vaccins, rappels et conformité aux schémas vaccinaux.

## Endpoints
- GET /v1/vaccinations/{patientId} : Carnet vaccinal
- POST /v1/vaccinations/{patientId} : Enregistrer vaccin
- GET /v1/vaccinations/{patientId}/due : Vaccins à faire
- GET /v1/vaccinations/campaigns : Campagnes vaccinales
- POST /v1/vaccinations/campaigns : Créer campagne

Authentification : apiKey