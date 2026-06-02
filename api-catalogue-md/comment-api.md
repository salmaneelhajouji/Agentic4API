# Comment API (comment-api)
Version v1 - statut : active
Domaine : Operations
Equipe : Equipe Platform

Commentaires et annotations sur des ressources internes (tickets, tâches, documents, contrats). Fils de discussion, mentions et réactions. DIFFÉRENCE vs review-api : Comment = annotation interne collaborative sur une ressource (ticket, doc), Review = avis public client sur un produit. DIFFÉRENCE vs messaging-api : Comment est ancré à une ressource spécifique (discussion contextualisée), Messaging est une conversation libre entre utilisateurs.

## Endpoints
- POST /v1/comments : Ajouter un commentaire sur une ressource
- GET /v1/comments/{resourceType}/{resourceId} : Commentaires d'une ressource
- PUT /v1/comments/{id} : Modifier un commentaire (auteur uniquement)
- DELETE /v1/comments/{id} : Supprimer un commentaire
- POST /v1/comments/{id}/reactions : Ajouter une réaction (👍, ✅, 🚀...)
- DELETE /v1/comments/{id}/reactions : Retirer sa réaction
- PUT /v1/comments/{id}/resolve : Résoudre un thread de commentaires

Authentification : Clé API Kong Gateway — Devoteam nexDigital