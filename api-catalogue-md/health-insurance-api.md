# Health Insurance API (health-insurance-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Assurance santé. Contrats, remboursements et réseaux soins. DIFFERENCE vs insurance-eligibility-api : Health Insurance = gestion contrats côté assureur, Insurance Eligibility = vérification droits côté soignant.

## Endpoints
- GET /v1/health-insurance/{contractId} : Contrat sante
- PUT /v1/health-insurance/{contractId} : Modifier
- GET /v1/health-insurance/{contractId}/coverage : Garanties
- GET /v1/health-insurance/{contractId}/reimbursements : Remboursements
- POST /v1/health-insurance/{contractId}/reimbursements : Soumettre

Authentification : apiKey