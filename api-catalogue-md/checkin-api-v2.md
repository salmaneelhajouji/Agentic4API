# Check-in API (checkin-api-v2)
Version v2 - statut : active
Domaine : Tourism
Equipe : Equipe Tourisme

Check-in et check-out hôtels. Mobile, clé digitale et documents. DIFFERENCE vs patient-admission-api : Checkin = accueil hôtel touristique, Patient Admission = admission hospitalière médicale.

## Endpoints
- POST /v2/checkin : Enregistrer depart
- GET /v2/checkin/{bookingId} : Statut
- POST /v2/checkin/{bookingId} : Clé digitale

Authentification : apiKey