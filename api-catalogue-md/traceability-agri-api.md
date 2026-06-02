# Traceability Agri API (traceability-agri-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Traçabilité agricole de la ferme au consommateur. Certifications et labels. DIFFERENCE vs logistics-tracking-api : Traceability Agri = origine produit agricole (parcelle, traitement), Logistics = suivi colis transport.

## Endpoints
- GET /v1/traceability/{productId} : Parcours ferme-consommateur
- GET /v1/traceability/{productId}/certificates : Certifications bio/HVE

Authentification : apiKey