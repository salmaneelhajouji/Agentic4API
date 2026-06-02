# Benefits API (benefits-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Avantages sociaux et mutuelle. Gestion des souscriptions aux avantages (mutuelle, tickets restaurant, etc.).

## Endpoints
- GET /v1/benefits : Catalogue des avantages disponibles
- GET /v1/benefits/{employeeId}/subscriptions : Avantages souscrits par un employé
- POST /v1/benefits/{employeeId}/subscriptions : Souscrire à un avantage
- DELETE /v1/benefits/{employeeId}/subscriptions/{id} : Se désinscrire d'un avantage

Authentification : apiKey