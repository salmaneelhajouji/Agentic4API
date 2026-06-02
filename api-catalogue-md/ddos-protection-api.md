# DDoS Protection API (ddos-protection-api)
Version v1 - statut : active
Domaine : Cybersecurity
Equipe : Equipe Cybersécurité

Protection contre les attaques DDoS. Detection, mitigation et rapports.

## Endpoints
- GET /v1/ddos/status : Statut protection
- GET /v1/ddos/attacks : Attaques détectées
- POST /v1/ddos/attacks : Signaler attaque
- GET /v1/ddos/rules : Règles mitigation
- POST /v1/ddos/rules : Ajouter règle
- GET /v1/ddos/reports : Rapport protection

Authentification : apiKey