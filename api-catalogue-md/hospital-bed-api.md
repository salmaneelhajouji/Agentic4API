# Hospital Bed API (hospital-bed-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Capacitaire hospitalier. Disponibilité des lits par service, admissions et taux d'occupation.

## Endpoints
- GET /v1/beds : Lits disponibles
- POST /v1/beds : Admettre dans un lit
- GET /v1/beds/{bedId} : Statut lit
- PUT /v1/beds/{bedId} : Changer statut
- DELETE /v1/beds/{bedId} : Libérer
- GET /v1/beds/occupancy : Taux d'occupation

Authentification : apiKey