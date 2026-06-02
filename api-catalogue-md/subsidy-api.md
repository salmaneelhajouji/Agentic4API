# Subsidy API (subsidy-api)
Version v1 - statut : active
Domaine : Agriculture
Equipe : Equipe Agriculture

Aides et subventions agricoles. PAC, MSA et dossiers.

## Endpoints
- GET /v1/subsidies : Aides disponibles
- GET /v1/subsidies/{farmId} : Aides exploitation
- POST /v1/subsidies/{farmId} : Demander aide
- GET /v1/subsidies/applications/{id} : Statut dossier
- PUT /v1/subsidies/applications/{id} : Mettre a jour

Authentification : apiKey