# Report API (report-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Rapport spécifique à une ressource métier — vue synthétique d'une entité (commande, client, projet). Génère un rapport contextuel sur demande. DIFFÉRENCE vs reporting-api : Reporting API génère des rapports périodiques planifiés sur des populations de données (ex: rapport mensuel des ventes), Report API génère un rapport contextuel instantané sur une ressource spécifique (ex: rapport de la commande ORD-0042). DIFFÉRENCE vs analytics-api : Analytics = exploration interactive de métriques agrégées, Report = document de synthèse sur une entité précise.

## Endpoints
- GET /v1/report/{resourceType}/{resourceId} : Générer un rapport contextuel sur une ressource
- POST /v1/report/batch : Générer plusieurs rapports en une fois
- GET /v1/report/templates : Templates de rapport disponibles par type de ressource
- POST /v1/report/templates : Créer un template de rapport custom
- POST /v1/report/scheduled : Planifier un rapport récurrent sur une ressource

Authentification : Clé API Kong Gateway — Devoteam nexDigital