# Analytics API (analytics-api-v3)
Version v3 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Version actuelle. Ajout de l'analytique prédictive ML, des alertes sur seuils de métriques, du partage de dashboards avec permissions granulaires et de l'intégration Looker/Tableau. DIFFÉRENCE vs reporting-api : Analytics = exploration temps réel et prédictions, Reporting = documents planifiés pour distribution.

## Endpoints
- GET /v3/analytics/sales : Métriques ventes avec détection d'anomalies
- POST /v3/analytics/predict : Prédictions ML sur les métriques (nouveau en v3)
- POST /v3/analytics/alerts : Créer alerte sur seuil de métrique (nouveau en v3)
- GET /v3/analytics/alerts : Lister les alertes actives
- POST /v3/analytics/export : Exporter vers Looker, Tableau ou PowerBI (nouveau en v3)
- POST /v3/analytics/dashboards : Créer dashboard avec permissions ACL

Authentification : Clé API Kong Gateway — Devoteam nexDigital