# Premium Calculation API (premium-calculation-api)
Version v1 - statut : active
Domaine : Insurance
Equipe : Equipe Assurance

Calcul primes d'assurance. Tarification actuarielle et comparaison.

## Endpoints
- POST /v1/premium/calculate : Calculer prime
- POST /v1/premium/compare : Comparer offres
- GET /v1/premium/{policyId} : Prime actuelle
- GET /v1/premium/history/{clientId} : Historique primes

Authentification : apiKey