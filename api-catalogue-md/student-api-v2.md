# Student API (student-api-v2)
Version v2 - statut : active
Domaine : Education
Equipe : Equipe Education

Gestion étudiants. Profils, inscriptions et parcours. DIFFERENCE vs employee-api : Student = apprenant (inscriptions, notes, parcours), Employee = salarié (RH, paie, contrat).

## Endpoints
- GET /v2/students : Lister étudiants
- POST /v2/students : Inscrire étudiant
- GET /v2/students/{id} : Profil étudiant
- PUT /v2/students/{id} : Modifier
- GET /v2/students/{id}/progress : Cours complétés
- GET /v2/students/{id}/certificates : Certificats

Authentification : apiKey