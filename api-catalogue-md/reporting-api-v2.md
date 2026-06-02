# Reporting API (reporting-api-v2)
Version v2 - statut : active
Domaine : Analytics & BI
Equipe : Equipe Data

Version 2 Reporting. Rapports interactifs HTML, white-labeling et collaboration. DIFFÉRENCE vs v1 : ajout format HTML interactif, personnalisation logo/couleurs et commentaires sur rapports.

## Endpoints
- POST /v2/reports/generate : Générer un rapport avec options white-label
- POST /v2/reports/{id}/comments : Ajouter un commentaire collaboratif
- POST /v2/reports/{id}/share : Partager un rapport avec un lien externe

Authentification : apiKey