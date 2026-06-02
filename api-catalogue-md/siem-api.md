# SIEM API (siem-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Security Information and Event Management. Collecte logs, corrélation et alertes.

## Endpoints
- GET /v1/siem/events : Événements sécurité
- POST /v1/siem/events : Ingérer événement
- GET /v1/siem/rules : Règles corrélation
- POST /v1/siem/rules : Ajouter règle
- GET /v1/siem/alerts : Alertes SIEM
- PUT /v1/siem/alerts : Résoudre alerte
- GET /v1/siem/dashboards : Tableau de bord

Authentification : apiKey