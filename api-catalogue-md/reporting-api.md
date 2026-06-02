# Reporting API (reporting-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Génération de rapports planifiés. Export PDF, Excel, tableaux de bord programmés. DIFFÉRENCE vs analytics-api : Reporting = documents générés et envoyés par email, Analytics = métriques consultables en temps réel.

## Endpoints
- POST /v1/reports/generate : Générer un rapport
- GET /v1/reports/{id} : Statut de génération
- GET /v1/reports/{id}/download : Télécharger le rapport
- POST /v1/reports/schedule : Planifier un rapport récurrent
- GET /v1/reports/templates : Modèles de rapports disponibles

Authentification : Clé API Kong Gateway