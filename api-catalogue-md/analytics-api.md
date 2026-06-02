# Analytics API (analytics-api)
Version v1 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Agrégation et reporting des données métier. KPIs ventes, trafic et comportement utilisateur. DIFFÉRENCE vs reporting-api : Analytics = métriques temps réel et historiques, Reporting = génération de documents PDF/Excel planifiés. DIFFÉRENCE vs metrics-api : Analytics = orienté business (ventes, conversion), Metrics = orienté ingénierie (latence, erreurs).

## Endpoints
- GET /v1/analytics/sales : Métriques de ventes
- GET /v1/analytics/traffic : Métriques de trafic
- GET /v1/analytics/conversion : Taux de conversion
- POST /v1/analytics/reports : Générer un rapport analytique personnalisé
- GET /v1/analytics/dashboard : Tableau de bord temps réel

Authentification : Clé API Kong Gateway