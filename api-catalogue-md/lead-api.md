# Lead API (lead-api)
Version v1 - statut : active
Domaine : CRM & Marketing
Equipe : Equipe CRM

Prospects et leads commerciaux. Scoring, qualification et pipeline de vente. DIFFÉRENCE vs crm-contact-api : Lead = prospects non-convertis en clients dans un pipeline de vente, Contact = toutes les relations existantes.

## Endpoints
- POST /v1/leads : Créer un lead
- GET /v1/leads : Lister les leads
- GET /v1/leads/{id} : Détails d'un lead
- PUT /v1/leads/{id}/qualify : Qualifier un lead
- PUT /v1/leads/{id}/assign : Assigner à un commercial
- GET /v1/leads/score/{id} : Score de qualification (0-100)

Authentification : Clé API Kong Gateway