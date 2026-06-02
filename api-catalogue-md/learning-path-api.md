# Learning Path API (learning-path-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Parcours d'apprentissage personnalisés. Recommandations IA et progression adaptative.

## Endpoints
- GET /v1/learning-paths : Parcours disponibles
- POST /v1/learning-paths : Créer parcours
- GET /v1/learning-paths/{id} : Detail parcours
- PUT /v1/learning-paths/{id} : Modifier
- GET /v1/learning-paths/recommend/{studentId} : Parcours recommandés
- GET /v1/learning-paths/{id}/progress/{studentId} : Progression

Authentification : apiKey