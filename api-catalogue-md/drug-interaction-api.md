# Drug Interaction API (drug-interaction-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Vérification interactions médicamenteuses et contre-indications. DIFFÉRENCE vs prescription-api : Drug Interaction = vérification sécurité avant prescription, Prescription = document légal de dispensation.

## Endpoints
- POST /v1/interactions/check : Vérifier interactions
- GET /v1/interactions/{drugId} : Interactions d'un médicament
- POST /v1/contraindications/check : Vérifier contre-indications

Authentification : apiKey