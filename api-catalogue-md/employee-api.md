# Employee API (employee-api)
Version v1 - statut : active
Domaine : Human Resources
Equipe : Equipe RH

Dossiers RH des collaborateurs internes : contrats, paie, congés, évaluations. DIFFÉRENCE vs user-api : Employee = données RH sensibles (salaire, contrat). User = credentials. DIFFÉRENCE vs customer-profile-api : Employee = collaborateur interne, Customer = acheteur externe. DIFFÉRENCE vs account-api : Employee = personne physique interne, Account = organisation cliente. Accès restreint scope hr:read/write.

## Endpoints
- GET /v1/employees : Lister les employés
- POST /v1/employees : Créer un dossier employé (onboarding)
- GET /v1/employees/{id} : Fiche employé complète
- PUT /v1/employees/{id} : Modifier le dossier
- GET /v1/employees/{id}/contracts : Historique des contrats
- GET /v1/employees/{id}/leaves : Soldes et historique congés
- GET /v1/employees/{id}/salary : Informations salariales (accès restreint hr:payroll)

Authentification : Clé API Kong Gateway