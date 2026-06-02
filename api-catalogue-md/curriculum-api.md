# Curriculum API (curriculum-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Programmes et curriculums. Référentiels de compétences et maquettes pédagogiques.

## Endpoints
- GET /v1/curricula : Programmes disponibles
- POST /v1/curricula : Créer programme
- GET /v1/curricula/{id} : Detail programme
- PUT /v1/curricula/{id} : Modifier
- GET /v1/curricula/{id}/competencies : Référentiel compétences
- POST /v1/curricula/{id}/competencies : Ajouter

Authentification : apiKey