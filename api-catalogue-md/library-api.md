# Library API (library-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Bibliothèque numérique. Catalogue, emprunts et ressources en ligne.

## Endpoints
- GET /v1/library/books : Rechercher
- POST /v1/library/books : Ajouter ouvrage
- GET /v1/library/books/{id} : Detail ouvrage
- POST /v1/library/books/{id} : Retourner
- GET /v1/library/loans/{studentId} : Emprunts étudiant
- GET /v1/library/digital : Ressources numériques

Authentification : apiKey