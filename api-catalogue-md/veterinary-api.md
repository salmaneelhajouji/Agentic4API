# Veterinary API (veterinary-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Services veterinaires elevage. Visites, vaccinations et prescriptions. DIFFERENCE vs allergy-api : Veterinary = soins animaux d'elevage, Allergy = allergies patients humains.

## Endpoints
- GET /v1/veterinary/{animalId} : Historique veterinaire
- POST /v1/veterinary/{animalId} : Ajouter visite
- GET /v1/veterinary/{animalId}/treatments : Traitements
- POST /v1/veterinary/{animalId}/treatments : Prescrire

Authentification : apiKey