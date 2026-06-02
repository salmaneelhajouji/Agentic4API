# Course API (course-api-v3)
Version v3 - statut : active
Domaine : Education
Equipe : Equipe Education

Cours e-learning complets. Modules, vidéos, quiz et certification. DIFFERENCE vs training-api : Course = formation académique e-learning, Training = formation professionnelle en entreprise.

## Endpoints
- GET /v3/courses : Catalogue cours
- POST /v3/courses : Créer cours
- GET /v3/courses/{id} : Detail cours
- PUT /v3/courses/{id} : Modifier
- DELETE /v3/courses/{id} : Supprimer
- GET /v3/courses/{id}/modules : Modules
- POST /v3/courses/{id}/modules : Ajouter module
- GET /v3/courses/{id}/quiz : Quiz
- POST /v3/courses/{id}/quiz : Soumettre réponses

Authentification : apiKey