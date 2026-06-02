# Damage Assessment API (damage-assessment-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Expertise et évaluation des dommages. Photos IA, rapport et montant. DIFFERENCE vs insurance-claim-api : Damage Assessment = expertise technique des dégâts, Claim = processus administratif indemnisation.

## Endpoints
- GET /v1/assessments : Expertises en cours
- POST /v1/assessments : Créer expertise
- GET /v1/assessments/{id} : Rapport expertise
- PUT /v1/assessments/{id} : Modifier
- POST /v1/assessments/{id}/photos : Analyser photos IA
- GET /v1/assessments/{id}/photos : Rapport dégâts

Authentification : apiKey