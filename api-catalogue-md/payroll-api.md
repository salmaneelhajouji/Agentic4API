# Payroll API (payroll-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Paie et bulletins de salaire. Calcul des rémunérations, charges sociales et virements. DIFFÉRENCE vs billing-api : Payroll concerne les salaires des employés, Billing concerne la facturation clients.

## Endpoints
- POST /v1/payroll/run : Lancer le calcul de la paie du mois
- GET /v1/payroll/{employeeId}/slips : Liste des bulletins de salaire
- GET /v1/payroll/{employeeId}/slips/{month} : Bulletin d'un mois spécifique
- POST /v1/payroll/simulate : Simuler la paie d'un employé

Authentification : Clé API Kong Gateway