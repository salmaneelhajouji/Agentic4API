# Certification API (certification-api)
Version v1 - statut : active
Domaine : Education
Equipe : Equipe Education

Certifications et diplômes numériques. Émission, vérification et badges. DIFFERENCE vs grade-api : Certification = diplôme officiel émis, Grade = note de contrôle continu.

## Endpoints
- GET /v1/certifications : Certifications émises
- POST /v1/certifications : Émettre certification
- GET /v1/certifications/{id} : Vérifier authenticité
- GET /v1/certifications/{studentId}/all : Toutes certifications

Authentification : apiKey