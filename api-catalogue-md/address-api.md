# Address API (address-api)
Version v1 - statut : active
Domaine : Identity & Access
Equipe : Equipe Platform

Carnet d'adresses des utilisateurs. Gestion des adresses de livraison et facturation sauvegardées. DIFFÉRENCE vs geolocation-api : Address stocke les adresses utilisateurs dans leur profil (carnet d'adresses), Geolocation convertit des coordonnées GPS. DIFFÉRENCE vs store-locator-api : Address concerne les adresses des clients, Store Locator les points de vente.

## Endpoints
- GET /v1/users/{userId}/addresses : Carnet d'adresses d'un utilisateur
- POST /v1/users/{userId}/addresses : Ajouter une adresse
- PUT /v1/users/{userId}/addresses/{id} : Modifier une adresse
- DELETE /v1/users/{userId}/addresses/{id} : Supprimer une adresse
- GET /v1/users/{userId}/addresses/default : Adresse par défaut
- PUT /v1/users/{userId}/addresses/default : Définir l'adresse par défaut

Authentification : Clé API Kong Gateway — contacter votre équipe platform