# Vital Signs API (vital-signs-api)
Version v1 - statut : active
Domaine : Healthcare
Equipe : Equipe Santé

Constantes physiologiques temps réel : tension, pouls, température, SpO2. DIFFÉRENCE vs lab-result-api : Vital Signs = mesures continues IoT médical, Lab = analyses biologiques ponctuelles.

## Endpoints
- GET /v1/vitals/{patientId} : Constantes récentes
- POST /v1/vitals/{patientId} : Enregistrer mesure
- GET /v1/vitals/{patientId}/alerts : Alertes seuils
- POST /v1/vitals/{patientId}/alerts : Configurer seuil

Authentification : apiKey