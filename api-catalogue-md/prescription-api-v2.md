# Prescription API (prescription-api-v2)
Version v2 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Ordonnances électroniques sécurisées avec signature numérique et envoi pharmacie. DIFFÉRENCE vs drug-interaction-api : Prescription = document légal, Drug Interaction = vérification incompatibilités.

## Endpoints
- GET /v2/prescriptions : Lister
- POST /v2/prescriptions : Créer ordonnance
- GET /v2/prescriptions/{id} : Détail
- PUT /v2/prescriptions/{id} : Modifier
- DELETE /v2/prescriptions/{id} : Annuler
- POST /v2/prescriptions/{id}/dispense : Marquer dispensée
- POST /v2/prescriptions/{id}/renew : Renouveler

Authentification : apiKey