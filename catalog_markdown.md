# ab-testing-api

**Titre** : A/B Testing API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Expérimentations et tests A/B. Variantes, assignation et analyse statistique des résultats.

## Endpoints
- **POST** /v1/experiments — Créer une expérience A/B
  - Requis : name, variants
  - Réponse : 201 — Créée
- **GET** /v1/experiments — Lister les expériences
  - Réponse : 200 — Expériences
- **GET** /v1/experiments/{id} — Détails d'une expérience
  - Requis : id
  - Réponse : 200 — Expérience
- **POST** /v1/experiments/{id}/assign — Assigner un utilisateur à une variante
  - Requis : id, user_id
  - Réponse : 200 — Variante assignée
- **POST** /v1/experiments/{id}/convert — Enregistrer une conversion
  - Requis : id, user_id, metric, value
  - Réponse : 200 — Conversion enregistrée
- **GET** /v1/experiments/{id}/results — Résultats statistiques de l'expérience
  - Requis : id
  - Réponse : 200 — Résultats avec p-value et uplift

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# access-review-api

**Titre** : Access Review API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Revue des accès et habilitations. Campagnes de certification et nettoyage.

## Endpoints
- **GET** /v1/access-reviews — Campagnes revue
  - Réponse : 200 — OK
- **POST** /v1/access-reviews — Lancer campagne
  - Réponse : 200 — OK
- **GET** /v1/access-reviews/{id} — Detail campagne
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/access-reviews/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/access-reviews/{id}/decisions — Décisions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/access-reviews/{id}/decisions — Soumettre décision
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/access-reviews/{id}/remediation — Actions correctives
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# accessibility-api

**Titre** : Accessibility API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Accessibilité numérique. Analyse WCAG, génération de descriptions alt-text et vérification de contrastes.

## Endpoints
- **POST** /v1/accessibility/analyze — Analyser l'accessibilité d'une page web
  - Requis : url
  - Réponse : 200 — Rapport d'accessibilité avec violations
- **POST** /v1/accessibility/alt-text — Générer du texte alternatif pour une image (IA)
  - Requis : image_url
  - Réponse : 200 — Alt-text généré
- **POST** /v1/accessibility/contrast — Vérifier le ratio de contraste couleur (WCAG)
  - Requis : foreground, background
  - Réponse : 200 — Ratio de contraste et conformité WCAG

## Authentification
ApiKeyAuth — apiKey

---

# account-api

**Titre** : Account API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Comptes organisations B2B. Gestion multi-utilisateurs sous une entité juridique (entreprise, association). Facturation, membres et rôles. DIFFÉRENCE vs user-api : Account = organisation (personne morale), User = personne physique. DIFFÉRENCE vs customer-profile-api : Account = entreprise cliente B2B, Customer = particulier B2C. DIFFÉRENCE vs employee-api : Account gère les clients entreprises, Employee les collaborateurs internes.

## Endpoints
- **POST** /v1/accounts — Créer un compte organisation
  - Réponse : 201 — Créé
- **GET** /v1/accounts — Lister les comptes organisations
  - Réponse : 200 — Liste
- **GET** /v1/accounts/{id} — Détails d'un compte
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/accounts/{id} — Mettre à jour un compte
  - Requis : id
  - Réponse : 200 — Mis à jour
- **GET** /v1/accounts/{id}/members — Lister les membres
  - Requis : id
  - Réponse : 200 — Membres
- **POST** /v1/accounts/{id}/members — Inviter un membre
  - Requis : id, email, role
  - Réponse : 202 — Invitation envoyée
- **GET** /v1/accounts/{id}/billing — Informations de facturation B2B
  - Requis : id
  - Réponse : 200 — Facturation
- **GET** /v1/accounts/{id}/usage — Consommation API du compte
  - Requis : id
  - Réponse : 200 — Consommation

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# activity-booking-api

**Titre** : Activity Booking API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Activités et loisirs. Réservation expériences, sports et culture.

## Endpoints
- **GET** /v1/activities — Activités disponibles
  - Réponse : 200 — OK
- **POST** /v1/activities — Référencer activité
  - Réponse : 200 — OK
- **GET** /v1/activities/{id} — Créneaux disponibles
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/activities/{id}/book — Réserver
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/activities/{id}/book — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# actuary-api

**Titre** : Actuary API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Calculs actuariels. Provisions, réserves et solvabilité.

## Endpoints
- **GET** /v1/actuary/provisions — Provisions techniques
  - Réponse : 200 — OK
- **POST** /v1/actuary/provisions — Calculer provisions
  - Réponse : 200 — OK
- **GET** /v1/actuary/solvency — Ratio solvabilite
  - Réponse : 200 — OK
- **POST** /v1/actuary/solvency — Tester solvabilite
  - Réponse : 200 — OK
- **GET** /v1/actuary/mortality — Tables mortalité
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# address-api

**Titre** : Address API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Platform

## Description
Carnet d'adresses des utilisateurs. Gestion des adresses de livraison et facturation sauvegardées. DIFFÉRENCE vs geolocation-api : Address stocke les adresses utilisateurs dans leur profil (carnet d'adresses), Geolocation convertit des coordonnées GPS. DIFFÉRENCE vs store-locator-api : Address concerne les adresses des clients, Store Locator les points de vente.

## Endpoints
- **GET** /v1/users/{userId}/addresses — Carnet d'adresses d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Adresses
- **POST** /v1/users/{userId}/addresses — Ajouter une adresse
  - Requis : userId
  - Réponse : 201 — Ajoutée
- **PUT** /v1/users/{userId}/addresses/{id} — Modifier une adresse
  - Requis : userId, id
  - Réponse : 200 — Modifiée
- **DELETE** /v1/users/{userId}/addresses/{id} — Supprimer une adresse
  - Requis : userId, id
  - Réponse : 204 — Supprimée
- **GET** /v1/users/{userId}/addresses/default — Adresse par défaut
  - Requis : userId
  - Réponse : 200 — Adresse par défaut
- **PUT** /v1/users/{userId}/addresses/default — Définir l'adresse par défaut
  - Requis : userId, address_id
  - Réponse : 200 — Définie

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# agri-marketplace-api

**Titre** : Agri Marketplace API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Marketplace agricole. Vente recoltes, intrants et materiel d'occasion.

## Endpoints
- **GET** /v1/agri-market/listings — Annonces
  - Réponse : 200 — OK
- **POST** /v1/agri-market/listings — Publier annonce
  - Réponse : 200 — OK
- **GET** /v1/agri-market/listings/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/agri-market/listings/{id} — Contacter vendeur
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# air-quality-api

**Titre** : Air Quality API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Qualité de l'air intérieur et extérieur. CO2, PM2.5, COV et indices AQI.

## Endpoints
- **GET** /v1/air-quality/{sensorId} — Données qualité air
  - Requis : sensorId
  - Réponse : 200 — OK
- **POST** /v1/air-quality/{sensorId} — Enregistrer
  - Requis : sensorId
  - Réponse : 200 — OK
- **GET** /v1/air-quality/{sensorId}/history — Historique
  - Requis : sensorId
  - Réponse : 200 — OK
- **GET** /v1/air-quality/alerts — Alertes
  - Réponse : 200 — OK
- **POST** /v1/air-quality/alerts — Créer alerte
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# alert-api

**Titre** : Alert API
**Version** : v1 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Alertes système et gestion des incidents. Pannes, seuils dépassés, escalades vers équipes OPS. DIFFÉRENCE vs notification-api : Alert cible les équipes techniques internes (PagerDuty, Slack ops), Notification cible les clients finaux. DIFFÉRENCE vs messaging-api : Alert est automatisé par des règles, Messaging est initié par un humain. DIFFÉRENCE vs email-api : Alert peut notifier par email mais son rôle est l'incident management.

## Endpoints
- **POST** /v1/alerts — Créer une alerte manuelle
  - Réponse : 201 — Créée
- **GET** /v1/alerts — Lister les alertes actives
  - Réponse : 200 — Alertes
- **PUT** /v1/alerts/{id}/acknowledge — Acquitter une alerte
  - Requis : id
  - Réponse : 200 — Acquittée
- **PUT** /v1/alerts/{id}/resolve — Résoudre une alerte
  - Requis : id
  - Réponse : 200 — Résolue
- **GET** /v1/alerts/rules — Lister les règles d'alerte
  - Réponse : 200 — Règles
- **POST** /v1/alerts/rules — Créer une règle d'alerte automatique
  - Réponse : 201 — Créée

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# allergy-api

**Titre** : Allergy API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Registre allergies et intolérances médicamenteuses et alimentaires. Alertes automatiques à la prescription.

## Endpoints
- **GET** /v1/allergies/{patientId} — Allergies du patient
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/allergies/{patientId} — Déclarer allergie
  - Requis : patientId
  - Réponse : 200 — OK
- **DELETE** /v1/allergies/{patientId} — Supprimer
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/allergies/{patientId}/check/{drugId} — Vérifier risque allergique
  - Requis : patientId, drugId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# alumni-api

**Titre** : Alumni API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Réseau anciens élèves. Annuaire, mentorat et événements alumni.

## Endpoints
- **GET** /v1/alumni — Anciens élèves
  - Réponse : 200 — OK
- **POST** /v1/alumni — S'inscrire
  - Réponse : 200 — OK
- **GET** /v1/alumni/{id} — Profil
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/alumni/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/alumni/mentoring — Mentors disponibles
  - Réponse : 200 — OK
- **POST** /v1/alumni/mentoring — Demander mentor
  - Réponse : 200 — OK
- **GET** /v1/alumni/events — Événements alumni
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# amenity-booking-api

**Titre** : Amenity Booking API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Réservation équipements partagés. Salles de réunion, parking, buanderie. DIFFERENCE vs meeting-room-api : Amenity Booking = équipements résidentiels, Meeting Room = salles de réunion professionnelles.

## Endpoints
- **GET** /v1/amenities — Equipements disponibles
  - Réponse : 200 — OK
- **GET** /v1/amenities/{id}/bookings — Réservations
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/amenities/{id}/bookings — Réserver
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/amenities/{id}/bookings/{bookingId} — Annuler
  - Requis : id, bookingId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# aml-api

**Titre** : AML API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Anti-Money Laundering. Surveillance transactions blanchiment et financement terrorisme. DIFFERENCE vs kyc-api : AML = monitoring continu, KYC = verification identite initiale.

## Endpoints
- **POST** /v1/aml/monitor — Analyser transaction
  - Réponse : 200 — OK
- **GET** /v1/aml/alerts — Alertes AML
  - Réponse : 200 — OK
- **PUT** /v1/aml/alerts — Ouvrir investigation
  - Réponse : 200 — OK
- **POST** /v1/aml/reports — Declaration TRACFIN
  - Réponse : 200 — OK
- **GET** /v1/aml/reports — Historique
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# aml-legal-api

**Titre** : AML Legal API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Lutte anti-blanchiment obligations professions juridiques. Declarations TRACFIN avocats/notaires. DIFFERENCE vs aml-api banque : AML Legal = obligations LCB-FT professions juridiques, AML = monitoring transactions bancaires.

## Endpoints
- **POST** /v1/aml-legal/screening — Cribler transaction
  - Réponse : 200 — OK
- **GET** /v1/aml-legal/declarations — Declarations TRACFIN
  - Réponse : 200 — OK
- **POST** /v1/aml-legal/declarations — Declarer au TRACFIN
  - Réponse : 200 — OK
- **GET** /v1/aml-legal/risk/{clientId} — Niveau risque client
  - Requis : clientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# analytics-api-v2

**Titre** : Analytics API
**Version** : v2 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Version 2 Analytics. Entonnoirs configurables, segments en temps réel, export streaming et dashboards partagés. DIFFÉRENCE vs v1 : ajout du streaming, des entonnoirs custom et du partage de dashboards.

## Endpoints
- **GET** /v2/analytics/sales — Métriques ventes v2
  - Réponse : 200 — Métriques
- **POST** /v2/analytics/funnels — Créer et analyser un entonnoir custom
  - Requis : steps
  - Réponse : 200 — Analyse entonnoir
- **POST** /v2/analytics/dashboard/share — Partager un dashboard avec un token d'accès public
  - Requis : dashboard_id
  - Réponse : 201 — Lien partageable généré
- **GET** /v2/analytics/stream — Métriques temps réel en streaming (Server-Sent Events)
  - Réponse : 200 — Stream SSE

## Authentification
ApiKeyAuth — apiKey

---

# analytics-api-v3

**Titre** : Analytics API
**Version** : v3 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Version actuelle. Ajout de l'analytique prédictive ML, des alertes sur seuils de métriques, du partage de dashboards avec permissions granulaires et de l'intégration Looker/Tableau. DIFFÉRENCE vs reporting-api : Analytics = exploration temps réel et prédictions, Reporting = documents planifiés pour distribution.

## Endpoints
- **GET** /v3/analytics/sales — Métriques ventes avec détection d'anomalies
  - Réponse : 200 — Métriques + anomalies détectées
- **POST** /v3/analytics/predict — Prédictions ML sur les métriques (nouveau en v3)
  - Requis : metric, horizon_days
  - Réponse : 200 — Prédictions avec intervalles de confiance
- **POST** /v3/analytics/alerts — Créer alerte sur seuil de métrique (nouveau en v3)
  - Requis : metric, condition, threshold
  - Réponse : 201 — Alerte créée
- **GET** /v3/analytics/alerts — Lister les alertes actives
  - Réponse : 200 — Alertes
- **POST** /v3/analytics/export — Exporter vers Looker, Tableau ou PowerBI (nouveau en v3)
  - Requis : destination
  - Réponse : 202 — Export lancé
- **POST** /v3/analytics/dashboards — Créer dashboard avec permissions ACL
  - Requis : name
  - Réponse : 201 — Dashboard créé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# analytics-api

**Titre** : Analytics API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Agrégation et reporting des données métier. KPIs ventes, trafic et comportement utilisateur. DIFFÉRENCE vs reporting-api : Analytics = métriques temps réel et historiques, Reporting = génération de documents PDF/Excel planifiés. DIFFÉRENCE vs metrics-api : Analytics = orienté business (ventes, conversion), Metrics = orienté ingénierie (latence, erreurs).

## Endpoints
- **GET** /v1/analytics/sales — Métriques de ventes
  - Réponse : 200 — Métriques ventes
- **GET** /v1/analytics/traffic — Métriques de trafic
  - Réponse : 200 — Trafic
- **GET** /v1/analytics/conversion — Taux de conversion
  - Réponse : 200 — Conversion
- **POST** /v1/analytics/reports — Générer un rapport analytique personnalisé
  - Réponse : 200 — Rapport
- **GET** /v1/analytics/dashboard — Tableau de bord temps réel
  - Réponse : 200 — Dashboard

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# anonymization-api

**Titre** : Anonymization API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Anonymisation RGPD. k-anonymite et masquage.

## Endpoints
- **POST** /v1/anonymize — Pseudonymiser
  - Réponse : 200 — OK
- **GET** /v1/anonymize/rules — Regles
  - Réponse : 200 — OK
- **POST** /v1/anonymize/rules — Creer
  - Réponse : 200 — OK
- **POST** /v1/anonymize/verify/{datasetId} — Verifier
  - Requis : datasetId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# api-gateway-api

**Titre** : API Gateway API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Gestion passerelle API. Routes, auth et monitoring.

## Endpoints
- **GET** /v1/gateway/routes — Routes
  - Réponse : 200 — OK
- **POST** /v1/gateway/routes — Ajouter route
  - Réponse : 200 — OK
- **GET** /v1/gateway/routes/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/gateway/routes/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/gateway/routes/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/gateway/consumers — Consommateurs
  - Réponse : 200 — OK
- **POST** /v1/gateway/consumers — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/gateway/analytics — Trafic API
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# api-key-api

**Titre** : API Key API
**Version** : v1 | **Statut** : active
**Domaine** : Security & Compliance | **Équipe** : Equipe Security

## Description
Gestion des clés API. Création, révocation, rotation et monitoring des usages.

## Endpoints
- **POST** /v1/api-keys — Créer une clé API
  - Requis : name, scopes
  - Réponse : 201 — Clé créée — affichée une seule fois
- **GET** /v1/api-keys — Lister les clés API
  - Réponse : 200 — Clés (sans les valeurs)
- **DELETE** /v1/api-keys/{id} — Révoquer une clé API
  - Requis : id
  - Réponse : 204 — Révoquée
- **POST** /v1/api-keys/{id}/rotate — Rotation sécurisée d'une clé API
  - Requis : id
  - Réponse : 200 — Nouvelle clé — ancienne révoquée dans 24h
- **GET** /v1/api-keys/{id}/usage — Historique d'utilisation d'une clé
  - Requis : id
  - Réponse : 200 — Usages

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# appointment-api

**Titre** : Appointment API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Prise de rendez-vous clients. Réservation de créneaux avec des conseillers ou techniciens. DIFFÉRENCE vs delivery-api : Appointment = RDV avec une personne (conseiller, technicien), Delivery = créneau de livraison de colis. DIFFÉRENCE vs calendar-api : Appointment gère les réservations côté client, Calendar gère les disponibilités internes.

## Endpoints
- **POST** /v1/appointments — Prendre un rendez-vous
  - Réponse : 201 — RDV pris
- **GET** /v1/appointments — Lister les rendez-vous
  - Réponse : 200 — Rendez-vous
- **GET** /v1/appointments/{id} — Détails d'un rendez-vous
  - Requis : id
  - Réponse : 200 — RDV | 404 — 
- **PUT** /v1/appointments/{id} — Reporter un rendez-vous
  - Requis : id, new_slot_id
  - Réponse : 200 — Reporté
- **DELETE** /v1/appointments/{id} — Annuler un rendez-vous
  - Requis : id
  - Réponse : 200 — Annulé
- **GET** /v1/appointments/slots — Créneaux disponibles
  - Requis : date
  - Réponse : 200 — Créneaux disponibles

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# assessment-api

**Titre** : Assessment API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Évaluations et examens. QCM, devoirs et corrections automatiques.

## Endpoints
- **GET** /v1/assessments — Évaluations
  - Réponse : 200 — OK
- **POST** /v1/assessments — Créer évaluation
  - Réponse : 200 — OK
- **GET** /v1/assessments/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/assessments/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/assessments/{id}/submissions — Rendus
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/assessments/{id}/submissions — Corriger
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# asset-management-api

**Titre** : Asset-Management API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Gestion actifs industriels. Immobilisations, amortissements et valeur residuelle. DIFFERENCE vs asset-tracking-api : Asset Management = valeur et comptabilite immobilisations, Asset Tracking = position GPS actifs.

## Endpoints
- **GET** /v1/assets-mgmt — Actifs
  - Réponse : 200 — OK
- **POST** /v1/assets-mgmt — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/assets-mgmt/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/assets-mgmt/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/assets-mgmt/{id}/depreciation — Amortissement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/assets-mgmt/{id}/depreciation — Calculer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# asset-tracking-api

**Titre** : Asset Tracking API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Suivi des actifs physiques en temps réel. GPS, géofencing et historique. DIFFERENCE vs logistics-tracking-api : Asset Tracking = actifs stationnaires (machines, équipements), Logistics = colis en transit.

## Endpoints
- **GET** /v1/assets — Lister actifs
  - Réponse : 200 — OK
- **POST** /v1/assets — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/assets/{id} — Position GPS
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/assets/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/assets/{id}/history — Historique positions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/assets/{id}/geofence — Créer zone
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/assets/{id}/geofence — Vérifier zone
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# attendance-api

**Titre** : Attendance API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Présences et absences. Suivi assiduité, justificatifs et alertes.

## Endpoints
- **GET** /v1/attendance/{studentId} — Présences
  - Requis : studentId
  - Réponse : 200 — OK
- **POST** /v1/attendance/{studentId} — Enregistrer
  - Requis : studentId
  - Réponse : 200 — OK
- **GET** /v1/attendance/{studentId}/absences — Absences
  - Requis : studentId
  - Réponse : 200 — OK
- **POST** /v1/attendance/{studentId}/absences — Justifier absence
  - Requis : studentId
  - Réponse : 200 — OK
- **GET** /v1/attendance/alerts — Alertes assiduité
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# attribution-api

**Titre** : Attribution API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Attribution marketing. Modèles first-touch, last-touch et multi-touch pour attribuer les conversions aux canaux.

## Endpoints
- **GET** /v1/attribution/models — Modèles d'attribution disponibles
  - Réponse : 200 — Modèles
- **POST** /v1/attribution/analyze — Analyser l'attribution d'une conversion
  - Requis : conversion_id, model
  - Réponse : 200 — Attribution calculée
- **GET** /v1/attribution/channels — Performance par canal sur une période
  - Réponse : 200 — Canaux

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# audit-log-api

**Titre** : Audit Log API
**Version** : v1 | **Statut** : active
**Domaine** : Security & Compliance | **Équipe** : Equipe Security

## Description
Journal d'audit et traçabilité. Toutes les actions sensibles enregistrées (qui a fait quoi, quand).

## Endpoints
- **GET** /v1/audit/logs — Consulter les logs d'audit
  - Réponse : 200 — Logs
- **POST** /v1/audit/export — Exporter les logs en CSV pour audit externe
  - Réponse : 202 — Export lancé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# auth-api-v1

**Titre** : Auth API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Version 1 de l'Auth API. DEPRECATED 2022. Sessions serveur sans JWT, pas de refresh token, pas d'OAuth2. Migrer vers v2 (JWT stateless).

## Endpoints
- **POST** /v1/auth/login — Connexion par session serveur (cookies)
  - Requis : email, password
  - Réponse : 200 — Cookie de session set-cookie | 401 — Identifiants invalides
- **POST** /v1/auth/logout — Déconnexion (invalidation session serveur)
  - Réponse : 204 — Déconnecté
- **GET** /v1/auth/me — Profil depuis session
  - Réponse : 200 — Profil

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# auth-api

**Titre** : Auth API
**Version** : v2 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Authentification et autorisation. Tokens JWT, OAuth2, refresh tokens et gestion des sessions.

## Endpoints
- **POST** /v2/auth/login — Authentifier un utilisateur et obtenir un JWT
  - Requis : email, password
  - Réponse : 200 — JWT + refresh token | 401 — Identifiants invalides
- **POST** /v2/auth/logout — Déconnecter et révoquer le token
  - Réponse : 204 — Déconnecté
- **POST** /v2/auth/refresh — Renouveler le JWT avec le refresh token
  - Requis : refresh_token
  - Réponse : 200 — Nouveau JWT | 401 — Refresh token expiré
- **GET** /v2/auth/me — Profil de l'utilisateur authentifié
  - Réponse : 200 — Profil
- **POST** /v2/auth/forgot-password — Initier la réinitialisation du mot de passe
  - Requis : email
  - Réponse : 202 — Email envoyé si le compte existe
- **POST** /v2/auth/reset-password — Réinitialiser le mot de passe avec le token reçu par email
  - Requis : token, new_password
  - Réponse : 200 — Réinitialisé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# auto-insurance-api

**Titre** : Auto Insurance API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Assurance automobile. Contrats, bonus-malus et constat amiable.

## Endpoints
- **GET** /v1/auto-insurance/{vehicleId} — Assurance véhicule
  - Requis : vehicleId
  - Réponse : 200 — OK
- **POST** /v1/auto-insurance/{vehicleId} — Souscrire
  - Requis : vehicleId
  - Réponse : 200 — OK
- **GET** /v1/auto-insurance/{contractId}/bonus-malus — Coefficient B/M
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/auto-insurance/accident-report — Créer constat amiable
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# backup-security-api

**Titre** : Backup Security API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Sauvegardes securisees. Chiffrement, immuabilite et tests de restauration.

## Endpoints
- **GET** /v1/backup/policies — Politiques backup
  - Réponse : 200 — OK
- **POST** /v1/backup/policies — Creer
  - Réponse : 200 — OK
- **GET** /v1/backup/jobs — Jobs backup
  - Réponse : 200 — OK
- **POST** /v1/backup/jobs — Lancer backup
  - Réponse : 200 — OK
- **POST** /v1/backup/restore — Test restauration
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# bancassurance-api

**Titre** : Bancassurance API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Produits bancassurance. Protection emprunts et assurances adossees credits.

## Endpoints
- **GET** /v1/bancassurance/products — Produits bancassurance
  - Réponse : 200 — OK
- **GET** /v1/bancassurance/{loanId}/coverage — Couverture pret
  - Requis : loanId
  - Réponse : 200 — OK
- **POST** /v1/bancassurance/{loanId}/coverage — Souscrire ADI
  - Requis : loanId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# bank-account-api-v1

**Titre** : Bank Account API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Comptes bancaires v1. DEPRECATED.

## Endpoints
- **GET** /v1/accounts — Lister
  - Réponse : 200 — OK
- **POST** /v1/accounts — Ouvrir
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# bank-account-api-v2

**Titre** : Bank Account API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Comptes bancaires v2 avec cloture.

## Endpoints
- **GET** /v2/accounts — Lister
  - Réponse : 200 — OK
- **POST** /v2/accounts — Ouvrir
  - Réponse : 200 — OK
- **GET** /v2/accounts/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/accounts/{id} — Cloturer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# bank-account-api-v3

**Titre** : Bank Account API
**Version** : v3 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Comptes courants et epargne avec open banking PSD2. DIFFERENCE vs wallet-api : Bank Account = compte bancaire IBAN/RIB, Wallet = portefeuille electronique interne.

## Endpoints
- **GET** /v3/accounts — Lister
  - Réponse : 200 — OK
- **POST** /v3/accounts — Ouvrir
  - Réponse : 200 — OK
- **GET** /v3/accounts/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/accounts/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/accounts/{id} — Cloturer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/accounts/{id}/transactions — Releve
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/accounts/{id}/transactions — Initier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# battery-storage-api

**Titre** : Battery Storage API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Systèmes de stockage batterie. Etat de charge, cycles et gestion énergie.

## Endpoints
- **GET** /v1/batteries — Lister
  - Réponse : 200 — OK
- **POST** /v1/batteries — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/batteries/{id} — Etat batterie
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/batteries/{id} — Mode charge/décharge
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/batteries/{id}/cycles — Historique cycles
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# benefits-api

**Titre** : Benefits API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Avantages sociaux et mutuelle. Gestion des souscriptions aux avantages (mutuelle, tickets restaurant, etc.).

## Endpoints
- **GET** /v1/benefits — Catalogue des avantages disponibles
  - Réponse : 200 — Avantages
- **GET** /v1/benefits/{employeeId}/subscriptions — Avantages souscrits par un employé
  - Requis : employeeId
  - Réponse : 200 — Souscriptions
- **POST** /v1/benefits/{employeeId}/subscriptions — Souscrire à un avantage
  - Requis : employeeId, benefit_id
  - Réponse : 201 — Souscrit
- **DELETE** /v1/benefits/{employeeId}/subscriptions/{id} — Se désinscrire d'un avantage
  - Requis : employeeId, id
  - Réponse : 200 — Désinscrit

## Authentification
ApiKeyAuth — apiKey

---

# billing-api-v2

**Titre** : Billing API
**Version** : v2 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version 2 de l'API facturation. Métered billing (usage-based), taxes automatiques et portail self-service. DIFFÉRENCE vs v1 : ajout facturation à l'usage, taxes auto via tax-api et portail client.

## Endpoints
- **POST** /v2/billing/subscriptions — Créer abonnement avec billing au usage
  - Requis : customer_id, plan_id
  - Réponse : 201 — Créé
- **POST** /v2/billing/usage — Reporter la consommation (métered billing)
  - Requis : subscription_id, quantity, metric
  - Réponse : 201 — Consommation enregistrée
- **POST** /v2/billing/portal/{customerId} — Générer un lien vers le portail self-service client
  - Requis : customerId
  - Réponse : 200 — URL du portail (valable 24h)

## Authentification
ApiKeyAuth — apiKey

---

# billing-api-v3

**Titre** : Billing API
**Version** : v3 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version actuelle recommandée. Ajout de la facturation hybride (flat + usage), du portail client self-service complet, de la gestion des crédits et avoirs automatiques, et de l'intégration ERP native. DIFFÉRENCE vs invoice-api : Billing orchestre les cycles de paiement récurrents, Invoice génère les documents fiscaux légaux.

## Endpoints
- **POST** /v3/billing/subscriptions — Créer abonnement hybride (flat + usage) avec workflow de relance
  - Réponse : 201 — Abonnement créé
- **GET** /v3/billing/subscriptions — Lister les abonnements
  - Réponse : 200 — Abonnements
- **GET** /v3/billing/subscriptions/{id} — Abonnement complet avec crédits et historique
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/billing/subscriptions/{id} — Modifier l'abonnement (upgrade/downgrade proratisé)
  - Requis : id
  - Réponse : 200 — Modifié
- **DELETE** /v3/billing/subscriptions/{id} — Résilier avec période de grâce
  - Requis : id
  - Réponse : 200 — Résilié
- **POST** /v3/billing/usage — Reporter consommation (métered billing)
  - Requis : subscription_id, quantity, metric
  - Réponse : 201 — Consommation enregistrée
- **POST** /v3/billing/credits — Émettre un crédit sur un abonnement (nouveau en v3)
  - Requis : subscription_id, amount, reason
  - Réponse : 201 — Crédit émis
- **POST** /v3/billing/erp-sync/{subscriptionId} — Forcer synchronisation ERP (SAP/Oracle/Sage — nouveau en v3)
  - Requis : subscriptionId, erp_system
  - Réponse : 202 — Sync ERP lancée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# billing-api

**Titre** : Billing API
**Version** : v1 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Cycles de facturation récurrents et abonnements. Prélèvements automatiques, relances impayés, gestion des plans. DIFFÉRENCE vs payment-api : Billing orchestre des paiements récurrents dans le temps, Payment traite une transaction ponctuelle. DIFFÉRENCE vs invoice-api : Billing déclenche les cycles, Invoice génère les PDFs. DIFFÉRENCE vs subscription-api : Billing gère le paiement, Subscription gère les droits d'accès.

## Endpoints
- **POST** /v1/billing/subscriptions — Créer un abonnement récurrent
  - Réponse : 201 — Créé
- **GET** /v1/billing/subscriptions/{customerId} — Abonnements actifs d'un client
  - Requis : customerId
  - Réponse : 200 — Abonnements
- **PUT** /v1/billing/subscriptions/{id}/cancel — Résilier un abonnement
  - Requis : id
  - Réponse : 200 — Résilié
- **GET** /v1/billing/invoices/{customerId} — Historique des factures
  - Requis : customerId
  - Réponse : 200 — Factures
- **POST** /v1/billing/retry/{invoiceId} — Relancer un paiement impayé
  - Requis : invoiceId
  - Réponse : 200 — Relance initiée | 402 — Refusé à nouveau

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# billing-telecom-api

**Titre** : Billing Telecom API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Facturation telecom. Factures, CDR et impayes. DIFFERENCE vs billing-api : Billing Telecom = usage telecom CDR/roaming, Billing = services generiques.

## Endpoints
- **GET** /v1/billing-telecom/{subscriberId} — Historique
  - Requis : subscriberId
  - Réponse : 200 — OK
- **GET** /v1/billing-telecom/{subscriberId}/cdr — Detail communications
  - Requis : subscriberId
  - Réponse : 200 — OK
- **POST** /v1/billing-telecom/{subscriberId}/disputes — Contester
  - Requis : subscriberId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# bom-api

**Titre** : BOM API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Bill of Materials nomenclatures. Multi-niveaux, variantes et gestion modifications.

## Endpoints
- **GET** /v1/bom/{productId} — Nomenclature
  - Requis : productId
  - Réponse : 200 — OK
- **POST** /v1/bom/{productId} — Creer nomenclature
  - Requis : productId
  - Réponse : 200 — OK
- **GET** /v1/bom/{productId}/components — Composants
  - Requis : productId
  - Réponse : 200 — OK
- **POST** /v1/bom/{productId}/components — Ajouter composant
  - Requis : productId
  - Réponse : 200 — OK
- **DELETE** /v1/bom/{productId}/components — Retirer
  - Requis : productId
  - Réponse : 200 — OK
- **GET** /v1/bom/{productId}/versions — Versions nomenclature
  - Requis : productId
  - Réponse : 200 — OK
- **POST** /v1/bom/{productId}/versions — Publier version
  - Requis : productId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# border-crossing-api

**Titre** : Border Crossing API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion passages frontaliers. Documents, files d'attente et temps de passage.

## Endpoints
- **GET** /v1/borders — Points de passage
  - Réponse : 200 — OK
- **GET** /v1/borders/{id} — Documents requis
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# broker-api

**Titre** : Broker API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Gestion courtiers et apporteurs. Commissions, mandats et portefeuilles.

## Endpoints
- **GET** /v1/brokers — Courtiers actifs
  - Réponse : 200 — OK
- **POST** /v1/brokers — Ajouter courtier
  - Réponse : 200 — OK
- **GET** /v1/brokers/{id} — Profile courtier
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/brokers/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/brokers/{id}/commission — Commissions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/brokers/{id}/commission — Calculer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/brokers/{id}/portfolio — Portefeuille client
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# building-automation-api

**Titre** : Building Automation API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Automatisation bâtiments intelligents. HVAC, éclairage, sécurité et accès.

## Endpoints
- **GET** /v1/buildings/{id} — Statut bâtiment
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/buildings/{id} — Mode eco/confort
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/buildings/{id}/zones — Zones du bâtiment
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/buildings/{id}/zones — Ajouter zone
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/buildings/{id}/energy — Consommation
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/buildings/{id}/alerts — Alertes
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# building-permit-api

**Titre** : Building Permit API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Permis de construire et autorisations urbanisme. Dépôt, suivi et conformité.

## Endpoints
- **GET** /v1/permits — Lister permis
  - Réponse : 200 — OK
- **POST** /v1/permits — Déposer demande
  - Réponse : 200 — OK
- **GET** /v1/permits/{id} — Statut instruction
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/permits/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/permits/{id}/documents — Documents
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/permits/{id}/documents — Ajouter document
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# bundle-api

**Titre** : Bundle API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Packs et bundles de produits. Création, tarification et gestion des lots.

## Endpoints
- **POST** /v1/bundles — Créer un bundle produit
  - Requis : name, products
  - Réponse : 201 — Bundle créé
- **GET** /v1/bundles — Lister les bundles
  - Réponse : 200 — Bundles
- **GET** /v1/bundles/{id} — Détails d'un bundle
  - Requis : id
  - Réponse : 200 — Bundle | 404 — 
- **PUT** /v1/bundles/{id} — Modifier
  - Requis : id
  - Réponse : 200 — Modifié
- **GET** /v1/bundles/{id}/price — Prix calculé du bundle avec remise automatique
  - Requis : id
  - Réponse : 200 — Prix du bundle

## Authentification
ApiKeyAuth — apiKey

---

# cache-api

**Titre** : Cache API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Gestion du cache distribué. Lecture, écriture, invalidation et TTL.

## Endpoints
- **GET** /v1/cache/{key} — Lire une valeur en cache
  - Requis : key
  - Réponse : 200 — Valeur | 404 — Clé non trouvée ou expirée
- **PUT** /v1/cache/{key} — Écrire une valeur en cache
  - Requis : key, value
  - Réponse : 200 — Enregistré
- **DELETE** /v1/cache/{key} — Invalider une clé de cache
  - Requis : key
  - Réponse : 204 — Invalidé
- **DELETE** /v1/cache/invalidate-prefix — Invalider toutes les clés avec un préfixe
  - Requis : prefix
  - Réponse : 200 — Invalidé
- **GET** /v1/cache/stats — Statistiques du cache (hit rate, mémoire)
  - Réponse : 200 — Stats

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# calendar-api

**Titre** : Calendar API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Gestion des calendriers et disponibilités internes. Plannings des conseillers, techniciens et ressources. DIFFÉRENCE vs appointment-api : Calendar = gestion des disponibilités et plannings côté équipes, Appointment = réservation côté client.

## Endpoints
- **GET** /v1/calendars/{resourceId} — Calendrier d'une ressource
  - Requis : resourceId
  - Réponse : 200 — Calendrier
- **GET** /v1/calendars/{resourceId}/availability — Disponibilités d'une ressource sur une période
  - Requis : resourceId, from, to
  - Réponse : 200 — Disponibilités
- **POST** /v1/calendars/{resourceId}/events — Ajouter un événement au calendrier
  - Requis : resourceId, title, start, end
  - Réponse : 201 — Événement créé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# campaign-api

**Titre** : Campaign API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe Marketing

## Description
Campagnes marketing multicanal. Création, segmentation, planification et analyse des performances.

## Endpoints
- **POST** /v1/campaigns — Créer une campagne
  - Réponse : 201 — Créée
- **GET** /v1/campaigns — Lister les campagnes
  - Réponse : 200 — Campagnes
- **GET** /v1/campaigns/{id} — Détails d'une campagne
  - Requis : id
  - Réponse : 200 — Campagne
- **PUT** /v1/campaigns/{id}/launch — Lancer une campagne
  - Requis : id
  - Réponse : 200 — Lancée
- **PUT** /v1/campaigns/{id}/pause — Mettre en pause
  - Requis : id
  - Réponse : 200 — Mise en pause
- **GET** /v1/campaigns/{id}/stats — Performances de la campagne
  - Requis : id
  - Réponse : 200 — Stats (open_rate, click_rate, conversions)

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# campus-api

**Titre** : Campus API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Services campus. Restaurants, salles, events et vie étudiante.

## Endpoints
- **GET** /v1/campus/facilities — Équipements campus
  - Réponse : 200 — OK
- **GET** /v1/campus/rooms — Salles disponibles
  - Réponse : 200 — OK
- **POST** /v1/campus/rooms — Réserver salle
  - Réponse : 200 — OK
- **GET** /v1/campus/events — Événements
  - Réponse : 200 — OK
- **POST** /v1/campus/events — Créer événement
  - Réponse : 200 — OK
- **GET** /v1/campus/canteen — Menu du jour
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# car-rental-api

**Titre** : Car Rental API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Location de voitures. Disponibilité, tarifs et contrats.

## Endpoints
- **GET** /v1/car-rental/vehicles — Véhicules disponibles
  - Réponse : 200 — OK
- **GET** /v1/car-rental/bookings — Réservations
  - Réponse : 200 — OK
- **POST** /v1/car-rental/bookings — Réserver véhicule
  - Réponse : 200 — OK
- **GET** /v1/car-rental/bookings/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/car-rental/bookings/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/car-rental/bookings/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/car-rental/bookings/{id}/contract — Contrat location
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# carbon-footprint-api

**Titre** : Carbon Footprint API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Empreinte carbone installations et activités. Calcul CO2, reporting ESG et recommandations.

## Endpoints
- **GET** /v1/carbon/{siteId} — Empreinte carbone
  - Requis : siteId
  - Réponse : 200 — OK
- **POST** /v1/carbon/{siteId} — Calculer
  - Requis : siteId
  - Réponse : 200 — OK
- **GET** /v1/carbon/{siteId}/report — Rapport ESG
  - Requis : siteId
  - Réponse : 200 — OK
- **POST** /v1/carbon/{siteId}/report — Générer rapport
  - Requis : siteId
  - Réponse : 200 — OK
- **GET** /v1/carbon/offsets — Compensations carbone
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# card-management-api

**Titre** : Card Management API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Cartes bancaires debit/credit. Activation, plafonds, opposition et cartes virtuelles.

## Endpoints
- **GET** /v1/cards/{clientId} — Cartes du client
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v1/cards/{clientId} — Commander
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/cards/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/cards/{id} — Modifier plafonds
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/cards/{id}/block — Opposition
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/cards/{id}/block — Lever opposition
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/cards/{id}/virtual — Carte virtuelle
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# care-plan-api

**Titre** : Care Plan API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Plans de soins personnalisés. Objectifs thérapeutiques, tâches et suivi observance.

## Endpoints
- **GET** /v1/care-plans/{patientId} — Plans actifs
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/care-plans/{patientId} — Créer plan
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/care-plans/{id}/tasks — Tâches du plan
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/care-plans/{id}/tasks — Ajouter tâche
  - Requis : id
  - Réponse : 200 — OK
- **PATCH** /v1/care-plans/{id}/tasks — Statut tâche
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# career-guidance-api

**Titre** : Career Guidance API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Orientation professionnelle. Metiers, competences et debouches.

## Endpoints
- **GET** /v1/careers/explore — Explorer metiers
  - Réponse : 200 — OK
- **POST** /v1/careers/explore — Matcher profil
  - Réponse : 200 — OK
- **GET** /v1/careers/{careerId} — Competences requises
  - Requis : careerId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# cargo-api-v1

**Titre** : Cargo API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Fret v1. DEPRECATED.

## Endpoints
- **GET** /v1/cargo — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# cargo-api-v2

**Titre** : Cargo API
**Version** : v2 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion fret et marchandises. Chargement, manifestes et suivi. DIFFERENCE vs shipping-api : Cargo = fret lourd/industriel (conteneurs, vrac), Shipping = colis e-commerce.

## Endpoints
- **GET** /v2/cargo — Lister cargaisons
  - Réponse : 200 — OK
- **POST** /v2/cargo — Créer cargaison
  - Réponse : 200 — OK
- **GET** /v2/cargo/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/cargo/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/cargo/{id}/manifest — Manifeste
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/cargo/{id}/manifest — Générer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/cargo/{id}/customs — Documents douane
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# cart-api

**Titre** : Cart API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Gestion du panier d'achat temporaire. Ajout, modification, suppression d'articles avant commande. Gère les sessions anonymes. DIFFÉRENCE vs order-api : Cart = panier temporaire avant achat, Order = commande confirmée après achat. DIFFÉRENCE vs wishlist-api : Cart = intention d'achat immédiate, Wishlist = désirs futurs sans intention immédiate.

## Endpoints
- **GET** /v1/cart/{userId} — Récupérer le panier d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Panier
- **POST** /v1/cart/{userId}/items — Ajouter un article au panier
  - Requis : userId
  - Réponse : 201 — Ajouté
- **PUT** /v1/cart/{userId}/items/{itemId} — Modifier la quantité d'un article
  - Requis : userId, itemId, quantity
  - Réponse : 200 — Modifié
- **DELETE** /v1/cart/{userId}/items/{itemId} — Supprimer un article du panier
  - Requis : userId, itemId
  - Réponse : 204 — Supprimé
- **POST** /v1/cart/{userId}/checkout — Valider le panier et créer une commande
  - Requis : userId
  - Réponse : 201 — Commande créée — panier vidé | 409 — Article en rupture de stock
- **DELETE** /v1/cart/{userId}/clear — Vider le panier
  - Requis : userId
  - Réponse : 204 — Vidé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# catalog-api

**Titre** : Catalog API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Gestion des catalogues et collections de produits destinés à la publication (site web, app, B2B). Un catalogue regroupe une sélection de produits avec ses propres règles de prix, de disponibilité et d'affichage. DIFFÉRENCE vs product-catalog-api : Catalog API gère les catalogues comme collections publiées (ex: catalogue été 2026, catalogue B2B Allemagne), Product Catalog API gère la taxonomie des catégories et attributs produits. DIFFÉRENCE vs product-api : Catalog = regroupement de produits existants en collections, Product = données d'un produit individuel.

## Endpoints
- **POST** /v1/catalogs — Créer un catalogue
  - Réponse : 201 — Catalogue créé
- **GET** /v1/catalogs — Lister les catalogues
  - Réponse : 200 — Catalogues
- **GET** /v1/catalogs/{id} — Détails d'un catalogue
  - Requis : id
  - Réponse : 200 — Catalogue | 404 — 
- **PUT** /v1/catalogs/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/catalogs/{id} — Archiver le catalogue
  - Requis : id
  - Réponse : 200 — Archivé
- **GET** /v1/catalogs/{id}/products — Produits d'un catalogue
  - Requis : id
  - Réponse : 200 — Produits
- **POST** /v1/catalogs/{id}/products — Ajouter des produits au catalogue
  - Requis : id, product_ids
  - Réponse : 200 — Ajoutés
- **DELETE** /v1/catalogs/{id}/products/{productId} — Retirer un produit du catalogue
  - Requis : id, productId
  - Réponse : 204 — Retiré
- **POST** /v1/catalogs/{id}/publish — Publier le catalogue (le rend visible sur les canaux)
  - Requis : id
  - Réponse : 200 — Publié

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# cdn-api

**Titre** : CDN API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Gestion du Content Delivery Network. Purge, règles de cache et statistiques.

## Endpoints
- **POST** /v1/cdn/purge — Purger des URLs ou préfixes du CDN
  - Réponse : 202 — Purge planifiée
- **GET** /v1/cdn/stats — Statistiques CDN (hit rate, bande passante)
  - Réponse : 200 — Stats
- **GET** /v1/cdn/rules — Règles de cache CDN
  - Réponse : 200 — Règles
- **POST** /v1/cdn/rules — Créer une règle de cache
  - Requis : path_pattern, ttl
  - Réponse : 201 — Règle créée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# cdr-api

**Titre** : CDR API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Detail communications CDR. DIFFERENCE vs billing-telecom-api : CDR = enregistrements bruts, Billing Telecom = factures.

## Endpoints
- **GET** /v1/cdr/calls — CDR appels
  - Réponse : 200 — OK
- **POST** /v1/cdr/calls — Exporter
  - Réponse : 200 — OK
- **GET** /v1/cdr/sms — CDR SMS
  - Réponse : 200 — OK
- **GET** /v1/cdr/data — CDR data
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# certificate-management-api

**Titre** : Certificate Management API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Gestion certificats SSL/TLS. Émission, renouvellement et révocation. DIFFERENCE vs key-rotation-api : Certificate Management = certificats X.509 PKI, Key Rotation = rotation clés cryptographiques.

## Endpoints
- **GET** /v1/certificates — Certificats actifs
  - Réponse : 200 — OK
- **POST** /v1/certificates — Émettre certificat
  - Réponse : 200 — OK
- **GET** /v1/certificates/{id} — Detail certificat
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/certificates/{id} — Renouveler
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/certificates/{id} — Révoquer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/certificates/expiring — Certificats expirant bientôt
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# certification-api

**Titre** : Certification API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Certifications et diplômes numériques. Émission, vérification et badges. DIFFERENCE vs grade-api : Certification = diplôme officiel émis, Grade = note de contrôle continu.

## Endpoints
- **GET** /v1/certifications — Certifications émises
  - Réponse : 200 — OK
- **POST** /v1/certifications — Émettre certification
  - Réponse : 200 — OK
- **GET** /v1/certifications/{id} — Vérifier authenticité
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/certifications/{studentId}/all — Toutes certifications
  - Requis : studentId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# chatbot-api

**Titre** : Chatbot API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Bot conversationnel. Intents, entités et réponses automatiques avant escalade humaine.

## Endpoints
- **POST** /v1/chatbot/message — Envoyer un message au chatbot
  - Requis : message, session_id
  - Réponse : 200 — Réponse du bot + intent détecté
- **GET** /v1/chatbot/intents — Lister les intentions configurées
  - Réponse : 200 — Intents
- **POST** /v1/chatbot/intents — Créer une intention
  - Requis : name, examples
  - Réponse : 201 — Intent créé
- **POST** /v1/chatbot/escalate — Escalader vers un agent humain
  - Requis : session_id
  - Réponse : 200 — Transfert vers live-chat-api

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# checkin-api-v1

**Titre** : Check-in API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Check-in v1. DEPRECATED.

## Endpoints
- **POST** /v1/checkin — Enregistrer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# checkin-api-v2

**Titre** : Check-in API
**Version** : v2 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Check-in et check-out hôtels. Mobile, clé digitale et documents. DIFFERENCE vs patient-admission-api : Checkin = accueil hôtel touristique, Patient Admission = admission hospitalière médicale.

## Endpoints
- **POST** /v2/checkin — Enregistrer depart
  - Réponse : 200 — OK
- **GET** /v2/checkin/{bookingId} — Statut
  - Requis : bookingId
  - Réponse : 200 — OK
- **POST** /v2/checkin/{bookingId} — Clé digitale
  - Requis : bookingId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# checkout-api

**Titre** : Checkout API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Tunnel d'achat et validation de commande. Orchestration du processus checkout : adresse, livraison, paiement. DIFFÉRENCE vs cart-api : Cart stocke les articles, Checkout orchestre les étapes de validation (adresse→livraison→paiement→confirmation). DIFFÉRENCE vs order-api : Checkout est le processus avant la commande, Order est le résultat après.

## Endpoints
- **POST** /v1/checkout/start — Démarrer une session checkout depuis le panier
  - Requis : cart_id
  - Réponse : 201 — Session checkout créée avec ID
- **PUT** /v1/checkout/{sessionId}/address — Étape 1 : Définir l'adresse de livraison
  - Requis : sessionId, shipping_address
  - Réponse : 200 — Adresse enregistrée
- **GET** /v1/checkout/{sessionId}/shipping — Étape 2 : Options de livraison disponibles
  - Requis : sessionId
  - Réponse : 200 — Options de livraison avec tarifs
- **PUT** /v1/checkout/{sessionId}/shipping — Sélectionner une option de livraison
  - Requis : sessionId, shipping_option_id
  - Réponse : 200 — Option sélectionnée
- **PUT** /v1/checkout/{sessionId}/payment — Étape 3 : Définir le moyen de paiement
  - Requis : sessionId, payment_method
  - Réponse : 200 — Paiement défini
- **POST** /v1/checkout/{sessionId}/confirm — Étape finale : Confirmer et créer la commande
  - Requis : sessionId
  - Réponse : 201 — Commande créée — order_id retourné | 402 — Paiement refusé | 409 — Stock insuffisant

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# claims-notification-api

**Titre** : Claims Notification API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Notifications sinistres. Alertes clients et partenaires. DIFFERENCE vs notification-api : Claims Notification = alertes specifiques assurance sinistre, Notification = multi-canaux generique.

## Endpoints
- **GET** /v1/claims-notifications/{claimId} — Notifications envoyees
  - Requis : claimId
  - Réponse : 200 — OK
- **POST** /v1/claims-notifications/{claimId} — Envoyer notification
  - Requis : claimId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# claims-settlement-api

**Titre** : Claims Settlement API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Règlement sinistres et indemnisation. Calcul, paiement et quittance.

## Endpoints
- **GET** /v1/settlements — Règlements en cours
  - Réponse : 200 — OK
- **POST** /v1/settlements — Initier règlement
  - Réponse : 200 — OK
- **GET** /v1/settlements/{id} — Detail règlement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/settlements/{id} — Payer indemnité
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/settlements/{id}/receipt — Quittance
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# claims-tracking-api

**Titre** : Claims Tracking API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Suivi temps reel sinistres. Statut, ETA et notifications client. DIFFERENCE vs insurance-claim-api : Claims Tracking = suivi statut client, Claim = gestion interne gestionnaire.

## Endpoints
- **GET** /v1/claims-tracking/{claimId} — Chronologie
  - Requis : claimId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# clinical-trial-api

**Titre** : Clinical Trial API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Essais cliniques. Protocoles, recrutement patients, suivi cohortes et rapports réglementaires EMA/FDA.

## Endpoints
- **GET** /v1/trials — Essais en cours
  - Réponse : 200 — OK
- **POST** /v1/trials — Créer protocole
  - Réponse : 200 — OK
- **GET** /v1/trials/{id} — Protocole complet
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/trials/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/trials/{id}/enroll — Inscrire patient
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/trials/{id}/enroll — Participants
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# co-living-api

**Titre** : Co-living API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion espaces co-living. Chambres, espaces partagés et services. DIFFERENCE vs hotel-api : Co-living = résidence longue durée avec espaces partagés, Hotel = hébergement touristique court séjour.

## Endpoints
- **GET** /v1/coliving/spaces — Espaces co-living
  - Réponse : 200 — OK
- **POST** /v1/coliving/spaces — Créer espace
  - Réponse : 200 — OK
- **GET** /v1/coliving/spaces/{id}/rooms — Chambres disponibles
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/coliving/spaces/{id}/rooms — Réserver chambre
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/coliving/spaces/{id}/amenities — Services
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# cohort-api

**Titre** : Cohort API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Analyse de cohortes clients. Rétention, LTV et comportement par groupe d'acquisition.

## Endpoints
- **POST** /v1/cohorts — Créer une analyse de cohorte
  - Requis : name, acquisition_period, metric
  - Réponse : 201 — Créée
- **GET** /v1/cohorts — Lister les cohortes
  - Réponse : 200 — Cohortes
- **GET** /v1/cohorts/{id}/retention — Matrice de rétention
  - Requis : id
  - Réponse : 200 — Matrice de rétention
- **GET** /v1/cohorts/{id}/ltv — LTV de la cohorte par période
  - Requis : id
  - Réponse : 200 — LTV

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# comment-api

**Titre** : Comment API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Commentaires et annotations sur des ressources internes (tickets, tâches, documents, contrats). Fils de discussion, mentions et réactions. DIFFÉRENCE vs review-api : Comment = annotation interne collaborative sur une ressource (ticket, doc), Review = avis public client sur un produit. DIFFÉRENCE vs messaging-api : Comment est ancré à une ressource spécifique (discussion contextualisée), Messaging est une conversation libre entre utilisateurs.

## Endpoints
- **POST** /v1/comments — Ajouter un commentaire sur une ressource
  - Réponse : 201 — Commentaire ajouté
- **GET** /v1/comments/{resourceType}/{resourceId} — Commentaires d'une ressource
  - Requis : resourceType, resourceId
  - Réponse : 200 — Commentaires
- **PUT** /v1/comments/{id} — Modifier un commentaire (auteur uniquement)
  - Requis : id, content
  - Réponse : 200 — Modifié
- **DELETE** /v1/comments/{id} — Supprimer un commentaire
  - Requis : id
  - Réponse : 204 — Supprimé
- **POST** /v1/comments/{id}/reactions — Ajouter une réaction (👍, ✅, 🚀...)
  - Requis : id, emoji
  - Réponse : 200 — Réaction ajoutée
- **DELETE** /v1/comments/{id}/reactions — Retirer sa réaction
  - Requis : id, emoji
  - Réponse : 204 — Retirée
- **PUT** /v1/comments/{id}/resolve — Résoudre un thread de commentaires
  - Requis : id
  - Réponse : 200 — Thread résolu

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# commodity-price-api

**Titre** : Commodity Price API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Prix matières premières agricoles. Cours marchés et historiques.

## Endpoints
- **GET** /v1/commodities — Matières premières
  - Réponse : 200 — OK
- **GET** /v1/commodities/{id}/price — Historique cours
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/commodities/alerts — Alertes prix
  - Réponse : 200 — OK
- **POST** /v1/commodities/alerts — Créer alerte
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# compliance-check-api

**Titre** : Compliance Check API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Conformité réglementaire. ISO 27001, RGPD, PCI-DSS et audits.

## Endpoints
- **POST** /v1/compliance/check — Lancer audit conformité
  - Réponse : 200 — OK
- **GET** /v1/compliance/frameworks — Référentiels disponibles
  - Réponse : 200 — OK
- **GET** /v1/compliance/reports/{orgId} — Rapport conformité
  - Requis : orgId
  - Réponse : 200 — OK
- **POST** /v1/compliance/reports/{orgId} — Générer rapport
  - Requis : orgId
  - Réponse : 200 — OK
- **GET** /v1/compliance/gaps — Écarts identifiés
  - Réponse : 200 — OK
- **POST** /v1/compliance/gaps — Plan correction
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# compliance-legal-api

**Titre** : Compliance Legal API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Conformite reglementaire juridique. Obligations, veille et reporting. DIFFERENCE vs compliance-check-api : Compliance Legal = conformite droit des affaires, Compliance Check = conformite securite informatique.

## Endpoints
- **GET** /v1/compliance/legal/obligations — Obligations legales
  - Réponse : 200 — OK
- **POST** /v1/compliance/legal/obligations — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/compliance/legal/{obligationId}/status — Statut conformite
  - Requis : obligationId
  - Réponse : 200 — OK
- **PUT** /v1/compliance/legal/{obligationId}/status — Mettre a jour
  - Requis : obligationId
  - Réponse : 200 — OK
- **GET** /v1/compliance/legal/reports — Rapports
  - Réponse : 200 — OK
- **POST** /v1/compliance/legal/reports — Générer rapport
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# concierge-api

**Titre** : Concierge API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Services conciergerie hôtelière. Réservations, recommandations et assistance.

## Endpoints
- **GET** /v1/concierge/{hotelId} — Services disponibles
  - Requis : hotelId
  - Réponse : 200 — OK
- **GET** /v1/concierge/{hotelId}/requests — Demandes en cours
  - Requis : hotelId
  - Réponse : 200 — OK
- **POST** /v1/concierge/{hotelId}/requests — Créer demande
  - Requis : hotelId
  - Réponse : 200 — OK
- **GET** /v1/concierge/{hotelId}/recommendations — Recommandations locales
  - Requis : hotelId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# config-api

**Titre** : Config API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Configuration applicative et feature flags.

## Endpoints
- **GET** /v1/config/{key} — Récupérer une configuration
  - Requis : key
  - Réponse : 200 — Valeur
- **PUT** /v1/config/{key} — Définir une configuration
  - Requis : key, value
  - Réponse : 200 — Défini
- **GET** /v1/config/features — Lister les feature flags
  - Réponse : 200 — Feature flags
- **PUT** /v1/config/features/{flag}/toggle — Activer/désactiver un feature flag
  - Requis : flag, enabled
  - Réponse : 200 — Togglé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# configuration-api

**Titre** : Configuration API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Gestion configuration applicative. Parametres, secrets et environnements.

## Endpoints
- **GET** /v1/config/{appId} — Config application
  - Requis : appId
  - Réponse : 200 — OK
- **PUT** /v1/config/{appId} — Mettre a jour
  - Requis : appId
  - Réponse : 200 — OK
- **GET** /v1/config/{appId}/{env} — Config par env
  - Requis : appId, env
  - Réponse : 200 — OK
- **PUT** /v1/config/{appId}/{env} — Definir config
  - Requis : appId, env
  - Réponse : 200 — OK
- **GET** /v1/config/{appId}/secrets — Secrets
  - Requis : appId
  - Réponse : 200 — OK
- **POST** /v1/config/{appId}/secrets — Definir secret
  - Requis : appId
  - Réponse : 200 — OK
- **DELETE** /v1/config/{appId}/secrets — Supprimer
  - Requis : appId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# contact-api

**Titre** : Contact API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Platform

## Description
Annuaire de contacts partagé de l'entreprise. Répertoire interne des collaborateurs, prestataires et partenaires — accessible depuis les applications. DIFFÉRENCE vs crm-contact-api : Contact API = annuaire interne en lecture (carnet d'adresses d'entreprise partagé), CRM Contact API = gestion complète des relations commerciales avec historique d'interactions. DIFFÉRENCE vs address-api : Contact = personne avec coordonnées complètes, Address = carnet d'adresses postales d'un utilisateur.

## Endpoints
- **GET** /v1/contacts — Lister l'annuaire de contacts
  - Réponse : 200 — Contacts
- **POST** /v1/contacts — Ajouter un contact à l'annuaire
  - Réponse : 201 — Contact créé
- **GET** /v1/contacts/{id} — Fiche contact
  - Requis : id
  - Réponse : 200 — Contact | 404 — 
- **PUT** /v1/contacts/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/contacts/{id} — Retirer de l'annuaire
  - Requis : id
  - Réponse : 204 — Supprimé
- **GET** /v1/contacts/{id}/vcard — Exporter la fiche contact en vCard (.vcf)
  - Requis : id
  - Réponse : 200 — Fichier vCard (.vcf)
- **POST** /v1/contacts/import — Importer des contacts en masse (CSV/vCard)
  - Réponse : 202 — Import lancé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# contact-form-api

**Titre** : Contact Form API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Formulaires de contact web et mobile. Réception, routing et conversion en tickets. DIFFÉRENCE vs ticket-api : Contact Form = point d'entrée côté client (formulaire), Ticket API = gestion interne des demandes (backoffice).

## Endpoints
- **POST** /v1/contact/submit — Soumettre un formulaire de contact
  - Réponse : 201 — Reçu — ticket créé automatiquement
- **GET** /v1/contact/forms — Lister les formulaires configurés
  - Réponse : 200 — Formulaires
- **POST** /v1/contact/forms — Créer un formulaire de contact
  - Requis : name, fields
  - Réponse : 201 — Formulaire créé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# contract-analytics-api

**Titre** : Contract Analytics API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Analyse contrats par IA. Extraction clauses, risques et comparaison. DIFFERENCE vs contract-api : Contract Analytics = analyse IA existants, Contract = gestion cycle de vie.

## Endpoints
- **POST** /v1/contract-analytics/{contractId} — Analyser contrat
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/contract-analytics/{contractId} — Risques identifies
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/contract-analytics/compare — Comparer contrats
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# contract-api-v1

**Titre** : Contract API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Contrats v1. DEPRECATED.

## Endpoints
- **GET** /v1/contracts — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# contract-api-v2

**Titre** : Contract API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Contrats v2 avec signature electronique. DEPRECATED.

## Endpoints
- **GET** /v2/contracts — Lister
  - Réponse : 200 — OK
- **POST** /v2/contracts — Créer
  - Réponse : 200 — OK
- **POST** /v2/contracts/{id}/sign — Signer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# contract-api-v3

**Titre** : Contract API
**Version** : v3 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Gestion contrats complets. Templates, negociation, signature et suivi. DIFFERENCE vs lease-api : Contract = contrat juridique generique, Lease = bail immobilier specifique.

## Endpoints
- **GET** /v3/contracts — Portefeuille contrats
  - Réponse : 200 — OK
- **POST** /v3/contracts — Créer contrat
  - Réponse : 200 — OK
- **GET** /v3/contracts/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/contracts/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/contracts/{id} — Terminer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/contracts/{id}/clauses — Clauses
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/contracts/{id}/clauses — Ajouter clause
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/contracts/{id}/sign — Signer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/contracts/{id}/sign — Statut signatures
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/contracts/{id}/amendments — Avenants
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/contracts/{id}/amendments — Créer avenant
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# contract-api

**Titre** : Contract API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Legal

## Description
Gestion des contrats juridiques. Rédaction, négociation, signature et suivi des échéances contractuelles. DIFFÉRENCE vs document-api : Contract API gère le cycle de vie juridique complet (négociation, versions, obligations, renouvellement), Document API génère des documents depuis des templates. DIFFÉRENCE vs invoice-api : Contract est un accord juridique entre parties, Invoice est un document fiscal de facturation.

## Endpoints
- **POST** /v1/contracts — Créer un contrat
  - Réponse : 201 — Contrat créé
- **GET** /v1/contracts — Lister les contrats
  - Réponse : 200 — Contrats
- **GET** /v1/contracts/{id} — Contrat complet avec historique de versions
  - Requis : id
  - Réponse : 200 — Contrat | 404 — 
- **PUT** /v1/contracts/{id} — Modifier le contrat (crée une nouvelle version)
  - Requis : id
  - Réponse : 200 — Nouvelle version créée
- **POST** /v1/contracts/{id}/sign — Envoyer en signature aux parties
  - Requis : id, signatories
  - Réponse : 202 — Invitations de signature envoyées
- **GET** /v1/contracts/{id}/obligations — Obligations contractuelles et échéances
  - Requis : id
  - Réponse : 200 — Obligations
- **POST** /v1/contracts/{id}/obligations — Ajouter une obligation (livrable, paiement, etc.)
  - Requis : id, title, due_date, type
  - Réponse : 201 — Obligation ajoutée
- **POST** /v1/contracts/{id}/renew — Renouveler un contrat expiré ou arrivant à terme
  - Requis : id, new_end_date
  - Réponse : 201 — Contrat renouvelé — nouvelle version créée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# coupon-api

**Titre** : Coupon API
**Version** : v1 | **Statut** : active
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Coupons et codes promo. Generation, validation et tracking.

## Endpoints
- **GET** /v1/coupons — Coupons actifs
  - Réponse : 200 — OK
- **POST** /v1/coupons — Creer coupon
  - Réponse : 200 — OK
- **GET** /v1/coupons/{code} — Detail coupon
  - Requis : code
  - Réponse : 200 — OK
- **POST** /v1/coupons/{code} — Utiliser coupon
  - Requis : code
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# course-api-v1

**Titre** : Course API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Cours v1. DEPRECATED.

## Endpoints
- **GET** /v1/courses — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# course-api-v2

**Titre** : Course API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Cours v2 avec modules. DEPRECATED.

## Endpoints
- **GET** /v2/courses — Lister
  - Réponse : 200 — OK
- **POST** /v2/courses — Créer
  - Réponse : 200 — OK
- **GET** /v2/courses/{id}/modules — Modules
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/courses/{id}/modules — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# course-api-v3

**Titre** : Course API
**Version** : v3 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Cours e-learning complets. Modules, vidéos, quiz et certification. DIFFERENCE vs training-api : Course = formation académique e-learning, Training = formation professionnelle en entreprise.

## Endpoints
- **GET** /v3/courses — Catalogue cours
  - Réponse : 200 — OK
- **POST** /v3/courses — Créer cours
  - Réponse : 200 — OK
- **GET** /v3/courses/{id} — Detail cours
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/courses/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/courses/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/courses/{id}/modules — Modules
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/courses/{id}/modules — Ajouter module
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/courses/{id}/quiz — Quiz
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/courses/{id}/quiz — Soumettre réponses
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# court-filing-api

**Titre** : Court Filing API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Dépôts et actes au tribunal. RPVA, e-barreau et suivi.

## Endpoints
- **GET** /v1/filings — Dépôts en cours
  - Réponse : 200 — OK
- **POST** /v1/filings — Créer dépôt
  - Réponse : 200 — OK
- **GET** /v1/filings/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/filings/{id} — Soumettre
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/filings/{id}/documents — Documents
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/filings/{id}/documents — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# credit-scoring-api

**Titre** : Credit Scoring API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Scoring credit et risque defaut. Modeles ML et notation Banque de France.

## Endpoints
- **GET** /v1/scoring/{clientId} — Score credit
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v1/scoring/{clientId} — Demander score
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v1/scoring/batch — Scoring en masse
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# crm-contact-api

**Titre** : CRM Contact API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe CRM

## Description
Contacts CRM : clients, prospects et partenaires. Segmentation, enrichissement et historique d'interactions. DIFFÉRENCE vs customer-profile-api : CRM Contact = vue 360° toutes relations (prospects, partenaires), Customer Profile = uniquement les acheteurs B2C.

## Endpoints
- **POST** /v1/crm/contacts — Créer un contact CRM
  - Réponse : 201 — Créé
- **GET** /v1/crm/contacts — Lister les contacts
  - Réponse : 200 — Contacts
- **GET** /v1/crm/contacts/{id} — Fiche contact
  - Requis : id
  - Réponse : 200 — Contact
- **PUT** /v1/crm/contacts/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/crm/contacts/{id} — Supprimer un contact
  - Requis : id
  - Réponse : 204 — Supprimé
- **POST** /v1/crm/contacts/search — Recherche avancée de contacts
  - Réponse : 200 — Résultats
- **GET** /v1/crm/contacts/{id}/interactions — Historique des interactions
  - Requis : id
  - Réponse : 200 — Interactions
- **POST** /v1/crm/contacts/{id}/interactions — Ajouter une interaction (appel, email, réunion)
  - Requis : id, type, summary
  - Réponse : 201 — Ajoutée

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# crop-api-v1

**Titre** : Crop API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Cultures v1. DEPRECATED.

## Endpoints
- **GET** /v1/crops — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# crop-api-v2

**Titre** : Crop API
**Version** : v2 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Gestion cultures et récoltes. Stades phénologiques, rendements et prévisions.

## Endpoints
- **GET** /v2/crops — Cultures en cours
  - Réponse : 200 — OK
- **POST** /v2/crops — Créer culture
  - Réponse : 200 — OK
- **GET** /v2/crops/{id} — Detail culture
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/crops/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/crops/{id}/phenology — Stade phénologique
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/crops/{id}/yield — Rendement réel
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/crops/{id}/yield — Prévoir rendement
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# crop-insurance-api

**Titre** : Crop Insurance API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Assurance récoltes. Grêle, sécheresse et sinistres. DIFFERENCE vs insurance-claim-api : Crop Insurance = assurance récolte agricole, Claim = sinistre assurance générique.

## Endpoints
- **GET** /v1/crop-insurance/contracts — Contrats récolte
  - Réponse : 200 — OK
- **POST** /v1/crop-insurance/contracts — Souscrire
  - Réponse : 200 — OK
- **GET** /v1/crop-insurance/claims — Sinistres récolte
  - Réponse : 200 — OK
- **POST** /v1/crop-insurance/claims — Déclarer perte
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# currency-exchange-api

**Titre** : Currency Exchange API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Change de devises. Taux temps réel, conversion et bureaux de change. DIFFERENCE vs interest-rate-api : Currency Exchange = taux change devises, Interest Rate = taux intérêt bancaires.

## Endpoints
- **GET** /v1/currency/rates — Taux de change
  - Réponse : 200 — OK
- **POST** /v1/currency/convert — Convertir montant
  - Réponse : 200 — OK
- **GET** /v1/currency/history/{pair} — Historique taux
  - Requis : pair
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# curriculum-api

**Titre** : Curriculum API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Programmes et curriculums. Référentiels de compétences et maquettes pédagogiques.

## Endpoints
- **GET** /v1/curricula — Programmes disponibles
  - Réponse : 200 — OK
- **POST** /v1/curricula — Créer programme
  - Réponse : 200 — OK
- **GET** /v1/curricula/{id} — Detail programme
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/curricula/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/curricula/{id}/competencies — Référentiel compétences
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/curricula/{id}/competencies — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# customer-care-api

**Titre** : Customer Care API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Service client telecom. Tickets, escalades et satisfaction.

## Endpoints
- **GET** /v1/care/tickets — Tickets
  - Réponse : 200 — OK
- **POST** /v1/care/tickets — Creer ticket
  - Réponse : 200 — OK
- **GET** /v1/care/tickets/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/care/tickets/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/care/tickets/{id} — Escalader
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# customer-journey-api

**Titre** : Customer Journey API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Parcours client omnicanal. Reconstruction des chemins d'achat et points de friction.

## Endpoints
- **GET** /v1/journey/{customerId} — Parcours complet d'un client
  - Requis : customerId
  - Réponse : 200 — Parcours avec tous les touchpoints
- **POST** /v1/journey/touchpoints — Enregistrer un touchpoint
  - Requis : customer_id, channel, action
  - Réponse : 202 — Enregistré
- **GET** /v1/journey/friction-points — Points de friction identifiés dans les parcours
  - Réponse : 200 — Points de friction et taux d'abandon

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# customer-profile-api-v2

**Titre** : Customer Profile API
**Version** : v2 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe CRM

## Description
Version 2 du profil client. Enrichit avec score de propension, tags comportementaux et champs RGPD explicites. DIFFÉRENCE vs v1 : ajout propensity_score, behavioral_tags, consent_status et historique des segments.

## Endpoints
- **GET** /v2/customers — Lister avec filtres enrichis (score, tags, consentement)
  - Réponse : 200 — Liste
- **POST** /v2/customers — Créer un profil client v2
  - Réponse : 201 — Créé
- **GET** /v2/customers/{id} — Profil enrichi d'un client
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v2/customers/{id} — Mettre à jour le profil
  - Requis : id
  - Réponse : 200 — Mis à jour
- **GET** /v2/customers/{id}/segment-history — Historique des changements de segment
  - Requis : id
  - Réponse : 200 — Historique
- **GET** /v2/customers/{id}/propensity — Score de propension à l'achat (ML)
  - Requis : id
  - Réponse : 200 — Score 0-1

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# customer-profile-api

**Titre** : Customer Profile API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe CRM

## Description
Profils commerciaux clients : segmentation VIP/Standard, points fidélité, historique d'achat, préférences marketing, conformité RGPD. DIFFÉRENCE vs user-api : Customer Profile = données commerciales, User = credentials techniques. DIFFÉRENCE vs account-api : Customer = particulier B2C, Account = entreprise B2B. DIFFÉRENCE vs employee-api : Customer = acheteur externe, Employee = collaborateur interne.

## Endpoints
- **GET** /v1/customers — Lister les profils clients
  - Réponse : 200 — Liste
- **POST** /v1/customers — Créer un profil commercial client
  - Réponse : 201 — Créé | 409 — 
- **GET** /v1/customers/{id} — Récupérer un profil client
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/customers/{id} — Mettre à jour le profil
  - Requis : id
  - Réponse : 200 — Mis à jour
- **PUT** /v1/customers/{id}/segment — Changer le segment commercial (VIP/Standard/Nouveau)
  - Requis : id, segment
  - Réponse : 200 — Segment mis à jour
- **DELETE** /v1/customers/{id}/gdpr/delete — Droit à l'oubli RGPD — anonymisation sous 72h
  - Requis : id
  - Réponse : 202 — Anonymisation planifiée
- **GET** /v1/customers/{id}/purchase-history — Historique d'achat agrégé
  - Requis : id
  - Réponse : 200 — Historique

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# customs-clearance-api

**Titre** : Customs Clearance API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Dédouanement marchandises. Déclarations douanières, droits et suivi.

## Endpoints
- **GET** /v1/customs/declarations — Déclarations en cours
  - Réponse : 200 — OK
- **POST** /v1/customs/declarations — Créer déclaration
  - Réponse : 200 — OK
- **GET** /v1/customs/declarations/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/customs/declarations/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/customs/declarations/{id} — Soumettre
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/customs/tariffs — Calculer droits et taxes
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# damage-assessment-api

**Titre** : Damage Assessment API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Expertise et évaluation des dommages. Photos IA, rapport et montant. DIFFERENCE vs insurance-claim-api : Damage Assessment = expertise technique des dégâts, Claim = processus administratif indemnisation.

## Endpoints
- **GET** /v1/assessments — Expertises en cours
  - Réponse : 200 — OK
- **POST** /v1/assessments — Créer expertise
  - Réponse : 200 — OK
- **GET** /v1/assessments/{id} — Rapport expertise
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/assessments/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/assessments/{id}/photos — Analyser photos IA
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/assessments/{id}/photos — Rapport dégâts
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-access-control-api

**Titre** : Data Access Control API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Controle acces donnees. RBAC, policies et audits acces. DIFFERENCE vs permission-api : Data Access Control = droits sur datasets, Permission = droits applicatifs generiques.

## Endpoints
- **GET** /v1/data-access/policies — Politiques acces
  - Réponse : 200 — OK
- **POST** /v1/data-access/policies — Creer
  - Réponse : 200 — OK
- **GET** /v1/data-access/{datasetId}/grants — Droits accordes
  - Requis : datasetId
  - Réponse : 200 — OK
- **POST** /v1/data-access/{datasetId}/grants — Accorder acces
  - Requis : datasetId
  - Réponse : 200 — OK
- **DELETE** /v1/data-access/{datasetId}/grants — Revoquer acces
  - Requis : datasetId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-api-gateway-api

**Titre** : Data API Gateway
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Passerelle APIs donnees. Routage requetes, caching et security.

## Endpoints
- **GET** /v1/data-gateway/routes — Routes
  - Réponse : 200 — OK
- **POST** /v1/data-gateway/routes — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/data-gateway/cache — Stats cache
  - Réponse : 200 — OK
- **POST** /v1/data-gateway/cache — Invalider cache
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-catalog-api-v1

**Titre** : Data Catalog API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Catalogue donnees v1. DEPRECATED.

## Endpoints
- **GET** /v1/datasets — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-catalog-api-v2

**Titre** : Data Catalog API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Catalogue v2 avec lineage. DEPRECATED.

## Endpoints
- **GET** /v2/datasets — Lister
  - Réponse : 200 — OK
- **POST** /v2/datasets — Ajouter
  - Réponse : 200 — OK
- **GET** /v2/datasets/{id}/lineage — Lineage
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-catalog-api-v3

**Titre** : Data Catalog API
**Version** : v3 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Catalogue donnees central. Metadonnees, lineage, qualite et gouvernance. DIFFERENCE vs metadata-api : Data Catalog = gouvernance enterprise, Metadata = metadonnees fichiers.

## Endpoints
- **GET** /v3/datasets — Catalogue
  - Réponse : 200 — OK
- **POST** /v3/datasets — Enregistrer
  - Réponse : 200 — OK
- **GET** /v3/datasets/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/datasets/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/datasets/{id} — Deprecer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/datasets/{id}/lineage — Lineage complet
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/datasets/{id}/quality — Score qualite
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/datasets/{id}/quality — Lancer controle
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/datasets/{id}/glossary — Termes metier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/datasets/{id}/glossary — Ajouter terme
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-export-api

**Titre** : Data Export API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Export massif de données en CSV, JSON ou Parquet. Jobs asynchrones et téléchargements sécurisés.

## Endpoints
- **POST** /v1/exports — Créer un job d'export
  - Requis : entity, format
  - Réponse : 202 — Job lancé
- **GET** /v1/exports/{jobId}/status — Statut du job d'export
  - Requis : jobId
  - Réponse : 200 — Statut
- **GET** /v1/exports/{jobId}/download — Télécharger le fichier d'export (lien valable 24h)
  - Requis : jobId
  - Réponse : 200 — Fichier | 202 — Export en cours | 410 — Lien expiré
- **DELETE** /v1/exports/{jobId} — Annuler un job d'export
  - Requis : jobId
  - Réponse : 204 — Annulé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# data-governance-api

**Titre** : Data Governance API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Gouvernance donnees. Policies, classifications et stewards.

## Endpoints
- **GET** /v1/governance/policies — Politiques
  - Réponse : 200 — OK
- **POST** /v1/governance/policies — Creer
  - Réponse : 200 — OK
- **GET** /v1/governance/classification — Classifications
  - Réponse : 200 — OK
- **POST** /v1/governance/classification — Classifier
  - Réponse : 200 — OK
- **GET** /v1/governance/stewards — Stewards
  - Réponse : 200 — OK
- **POST** /v1/governance/stewards — Assigner
  - Réponse : 200 — OK
- **GET** /v1/governance/compliance — Rapport
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-lake-api

**Titre** : Data Lake API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Data lake. Zones, partitions et acces. DIFFERENCE vs data-warehouse-api : Data Lake = donnees brutes non structurees, Data Warehouse = donnees structurees agregees.

## Endpoints
- **GET** /v1/datalake/zones — Zones
  - Réponse : 200 — OK
- **POST** /v1/datalake/zones — Creer
  - Réponse : 200 — OK
- **GET** /v1/datalake/zones/{zone}/objects — Objets
  - Requis : zone
  - Réponse : 200 — OK
- **POST** /v1/datalake/zones/{zone}/objects — Uploader
  - Requis : zone
  - Réponse : 200 — OK
- **DELETE** /v1/datalake/zones/{zone}/objects — Supprimer
  - Requis : zone
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-lineage-api

**Titre** : Data Lineage API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Lignage end-to-end. DIFFERENCE vs data-catalog-api : Data Lineage = tracabilite flux, Data Catalog = inventaire.

## Endpoints
- **GET** /v1/lineage/{datasetId} — Complet
  - Requis : datasetId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-loss-prevention-api

**Titre** : Data Loss Prevention API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Prévention fuite de données. Détection, blocage et alertes DLP.

## Endpoints
- **GET** /v1/dlp/policies — Politiques DLP
  - Réponse : 200 — OK
- **POST** /v1/dlp/policies — Créer politique
  - Réponse : 200 — OK
- **GET** /v1/dlp/incidents — Incidents DLP
  - Réponse : 200 — OK
- **POST** /v1/dlp/incidents — Signaler
  - Réponse : 200 — OK
- **GET** /v1/dlp/incidents/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/dlp/incidents/{id} — Résoudre
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/dlp/scan — Scanner données
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-marketplace-api

**Titre** : Data Marketplace API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Marketplace interne donnees. Publication et abonnement.

## Endpoints
- **GET** /v1/marketplace/datasets — Parcourir
  - Réponse : 200 — OK
- **POST** /v1/marketplace/datasets — Publier
  - Réponse : 200 — OK
- **GET** /v1/marketplace/datasets/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/marketplace/datasets/{id} — S'abonner
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/marketplace/subscriptions — Mes abonnements
  - Réponse : 200 — OK
- **DELETE** /v1/marketplace/subscriptions — Se desabonner
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-processing-agreement-api

**Titre** : Data Processing Agreement API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Accords de traitement de donnees RGPD. DPA sous-traitants et gestion consentements. DIFFERENCE vs gdpr-api : DPA = contrat entre responsable et sous-traitant, GDPR = droits des personnes concernees.

## Endpoints
- **GET** /v1/dpa — DPA en vigueur
  - Réponse : 200 — OK
- **POST** /v1/dpa — Créer DPA
  - Réponse : 200 — OK
- **GET** /v1/dpa/{id} — Detail DPA
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/dpa/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/dpa/{id} — Signer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/dpa/{id}/processors — Sous-traitants
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/dpa/{id}/processors — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-profiling-api

**Titre** : Data Profiling API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Profilage donnees. Statistiques, distributions et patterns.

## Endpoints
- **POST** /v1/profiling/{datasetId} — Lancer profilage
  - Requis : datasetId
  - Réponse : 200 — OK
- **GET** /v1/profiling/{datasetId} — Resultats
  - Requis : datasetId
  - Réponse : 200 — OK
- **GET** /v1/profiling/{datasetId}/statistics — Taux nullite
  - Requis : datasetId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-quality-api

**Titre** : Data Quality API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Qualite des donnees. Regles et anomalies. DIFFERENCE vs data-catalog-api : Data Quality = controles qualite, Data Catalog = gouvernance inventaire.

## Endpoints
- **GET** /v1/quality/rules — Regles
  - Réponse : 200 — OK
- **POST** /v1/quality/rules — Creer
  - Réponse : 200 — OK
- **POST** /v1/quality/checks/{datasetId} — Lancer
  - Requis : datasetId
  - Réponse : 200 — OK
- **GET** /v1/quality/checks/{datasetId} — Resultats
  - Requis : datasetId
  - Réponse : 200 — OK
- **GET** /v1/quality/anomalies — Anomalies
  - Réponse : 200 — OK
- **PUT** /v1/quality/anomalies — Acquitter
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-sharing-api

**Titre** : Data Sharing API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Partage securise de donnees. Accords, acces controles et expiration.

## Endpoints
- **GET** /v1/data-sharing/agreements — Accords
  - Réponse : 200 — OK
- **POST** /v1/data-sharing/agreements — Creer accord
  - Réponse : 200 — OK
- **GET** /v1/data-sharing/agreements/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/data-sharing/agreements/{id} — Revoquer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-usage-api

**Titre** : Data Usage API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Consommation data mobile. Quotas et throttling.

## Endpoints
- **GET** /v1/data-usage/{lineId} — Quota restant
  - Requis : lineId
  - Réponse : 200 — OK
- **GET** /v1/data-usage/{lineId}/history — Historique
  - Requis : lineId
  - Réponse : 200 — OK
- **GET** /v1/data-usage/{lineId}/throttling — Statut
  - Requis : lineId
  - Réponse : 200 — OK
- **POST** /v1/data-usage/{lineId}/throttling — Appliquer
  - Requis : lineId
  - Réponse : 200 — OK
- **DELETE** /v1/data-usage/{lineId}/throttling — Lever
  - Requis : lineId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-versioning-api

**Titre** : Data Versioning API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Versioning datasets. Snapshots, diff et rollback.

## Endpoints
- **GET** /v1/versioning/{datasetId} — Versions
  - Requis : datasetId
  - Réponse : 200 — OK
- **POST** /v1/versioning/{datasetId} — Creer snapshot
  - Requis : datasetId
  - Réponse : 200 — OK
- **GET** /v1/versioning/{datasetId}/{version} — Detail version
  - Requis : datasetId, version
  - Réponse : 200 — OK
- **POST** /v1/versioning/{datasetId}/{version} — Rollback
  - Requis : datasetId, version
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# data-warehouse-api

**Titre** : Data Warehouse API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Entrepot donnees structure. Tables, vues et requetes BI. DIFFERENCE vs data-lake-api : Data Warehouse = donnees structurees pour BI, Data Lake = donnees brutes.

## Endpoints
- **GET** /v1/warehouse/schemas — Schemas
  - Réponse : 200 — OK
- **POST** /v1/warehouse/schemas — Creer
  - Réponse : 200 — OK
- **GET** /v1/warehouse/tables/{schema} — Tables
  - Requis : schema
  - Réponse : 200 — OK
- **POST** /v1/warehouse/tables/{schema} — Creer
  - Requis : schema
  - Réponse : 200 — OK
- **POST** /v1/warehouse/query — Executer SQL
  - Réponse : 200 — OK
- **GET** /v1/warehouse/query — Historique
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# ddos-protection-api

**Titre** : DDoS Protection API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Protection contre les attaques DDoS. Detection, mitigation et rapports.

## Endpoints
- **GET** /v1/ddos/status — Statut protection
  - Réponse : 200 — OK
- **GET** /v1/ddos/attacks — Attaques détectées
  - Réponse : 200 — OK
- **POST** /v1/ddos/attacks — Signaler attaque
  - Réponse : 200 — OK
- **GET** /v1/ddos/rules — Règles mitigation
  - Réponse : 200 — OK
- **POST** /v1/ddos/rules — Ajouter règle
  - Réponse : 200 — OK
- **GET** /v1/ddos/reports — Rapport protection
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# delivery-api

**Titre** : Delivery API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Créneaux de livraison et planning. Réservation de plages horaires et gestion des livreurs. DIFFÉRENCE vs shipping-api : Delivery = planning des créneaux et livreurs, Shipping = colis et transporteurs.

## Endpoints
- **GET** /v1/delivery/slots — Créneaux de livraison disponibles
  - Requis : date, zip
  - Réponse : 200 — Créneaux
- **POST** /v1/delivery/book — Réserver un créneau de livraison
  - Requis : order_id, slot_id
  - Réponse : 201 — Créneau réservé
- **PUT** /v1/delivery/{id}/reschedule — Modifier le créneau de livraison
  - Requis : id, new_slot_id
  - Réponse : 200 — Reprogrammé
- **GET** /v1/delivery/tracking/{id} — Suivi en temps réel du livreur
  - Requis : id
  - Réponse : 200 — Position et ETA

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# demand-forecast-api

**Titre** : Demand Forecast API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Supply

## Description
Prévision de la demande. Modèles ML pour anticiper les besoins de stock et optimiser les achats.

## Endpoints
- **POST** /v1/forecast/demand — Générer une prévision de demande
  - Requis : product_ids, horizon_days
  - Réponse : 200 — Prévisions par produit et par jour
- **GET** /v1/forecast/stockouts — Produits à risque de rupture dans les 30 jours
  - Réponse : 200 — Produits à risque avec probabilité
- **POST** /v1/forecast/replenishment — Plan de réapprovisionnement recommandé
  - Réponse : 200 — Plan avec quantités recommandées par produit

## Authentification
ApiKeyAuth — apiKey

---

# demand-response-api

**Titre** : Demand Response API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Effacement et flexibilité énergétique. Programmes demand response et rémunération.

## Endpoints
- **GET** /v1/programs — Programmes DR disponibles
  - Réponse : 200 — OK
- **POST** /v1/programs — S'inscrire
  - Réponse : 200 — OK
- **GET** /v1/programs/{id}/events — Evénements en cours
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/programs/{id}/events — Activer effacement
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/programs/{id}/rewards — Récompenses accumulées
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# destination-api

**Titre** : Destination API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Informations destinations touristiques. Guides, météo et événements locaux.

## Endpoints
- **GET** /v1/destinations — Destinations
  - Réponse : 200 — OK
- **GET** /v1/destinations/{id} — Événements locaux
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/destinations/{id}/weather — Météo
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/destinations/{id}/attractions — Points intérêt
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# device-registry-api

**Titre** : Device Registry API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Registre des appareils IoT. Enregistrement, provisioning et gestion du cycle de vie.

## Endpoints
- **GET** /v1/devices — Lister appareils
  - Réponse : 200 — OK
- **POST** /v1/devices — Enregistrer appareil
  - Réponse : 200 — OK
- **GET** /v1/devices/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/devices/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/devices/{id} — Désactiver
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/devices/{id}/firmware — Version firmware
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/devices/{id}/firmware — Mise a jour
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# diagnosis-api

**Titre** : Diagnosis API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Aide au diagnostic médical. Codification CIM-10/CIM-11, suggestions IA et arbres de décision clinique.

## Endpoints
- **GET** /v1/diagnoses/{patientId} — Diagnostics du patient
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/diagnoses/{patientId} — Poser diagnostic
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/diagnoses/suggest — Suggestion diagnostique IA
  - Réponse : 200 — OK
- **GET** /v1/diagnoses/icd/{code} — Informations code CIM-11
  - Requis : code
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# discharge-api

**Titre** : Discharge API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Sortie du patient. Document de sortie, ordonnances de sortie et transmission médecin traitant.

## Endpoints
- **POST** /v1/discharge/{patientId} — Initier sortie
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/discharge/{patientId} — Statut
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/discharge/{patientId}/document — Document PDF
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/discharge/{patientId}/document — Générer
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/discharge/{patientId}/prescriptions — Ordonnances sortie
  - Requis : patientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# discount-api

**Titre** : Discount API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Marketing

## Description
Campagnes de remise et codes de réduction. Création, activation et suivi des promotions. DIFFÉRENCE vs pricing-api : Discount gère les campagnes et codes promo, Pricing calcule le prix final en intégrant toutes les règles dont les remises.

## Endpoints
- **POST** /v1/discounts — Créer un code de réduction
  - Réponse : 201 — Créé
- **GET** /v1/discounts/{code} — Détails d'un code promo
  - Requis : code
  - Réponse : 200 — OK
- **PUT** /v1/discounts/{id}/activate — Activer un code promo
  - Requis : id
  - Réponse : 200 — Activé
- **PUT** /v1/discounts/{id}/deactivate — Désactiver un code promo
  - Requis : id
  - Réponse : 200 — Désactivé
- **GET** /v1/discounts/campaigns — Lister les campagnes promotionnelles
  - Réponse : 200 — Campagnes

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# dispatch-api

**Titre** : Dispatch API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Dispatch et affectation missions. Optimisation affectations conducteurs/véhicules/missions.

## Endpoints
- **GET** /v1/missions — Missions disponibles
  - Réponse : 200 — OK
- **POST** /v1/missions — Créer mission
  - Réponse : 200 — OK
- **GET** /v1/missions/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/missions/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/missions/{id}/assign — Affecter conducteur
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/missions/{id}/assign — Désaffecter
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/dispatch/optimize — Optimiser affectations
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# dispute-resolution-api

**Titre** : Dispute Resolution API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Resolution amiable des litiges. Mediation, arbitrage et conciliation.

## Endpoints
- **GET** /v1/disputes — Differends en cours
  - Réponse : 200 — OK
- **POST** /v1/disputes — Ouvrir differend
  - Réponse : 200 — OK
- **GET** /v1/disputes/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/disputes/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/disputes/{id}/mediation — Clore sans accord
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# dns-api

**Titre** : DNS API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Gestion des enregistrements DNS. A, CNAME, MX et TTL.

## Endpoints
- **GET** /v1/dns/zones — Lister les zones DNS
  - Réponse : 200 — Zones
- **POST** /v1/dns/zones — Créer une zone DNS
  - Requis : domain
  - Réponse : 201 — Zone créée
- **GET** /v1/dns/zones/{zone}/records — Enregistrements d'une zone
  - Requis : zone
  - Réponse : 200 — Enregistrements
- **POST** /v1/dns/zones/{zone}/records — Ajouter un enregistrement DNS
  - Requis : zone, type, name, value, ttl
  - Réponse : 201 — Enregistrement ajouté
- **PUT** /v1/dns/zones/{zone}/records/{id} — Modifier un enregistrement
  - Requis : zone, id
  - Réponse : 200 — Modifié
- **DELETE** /v1/dns/zones/{zone}/records/{id} — Supprimer un enregistrement
  - Requis : zone, id
  - Réponse : 204 — Supprimé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# document-api

**Titre** : Document API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Génération de documents (contrats, CGV, devis). Templates Word/PDF et signature électronique. DIFFÉRENCE vs file-storage-api : Document API génère des documents à partir de templates, File Storage stocke des fichiers existants.

## Endpoints
- **POST** /v1/documents/generate — Générer un document depuis un template
  - Requis : template_id, data
  - Réponse : 201 — Document généré
- **GET** /v1/documents/templates — Lister les templates disponibles
  - Réponse : 200 — Templates
- **POST** /v1/documents/templates — Créer un template document
  - Requis : name, content
  - Réponse : 201 — Template créé
- **POST** /v1/documents/{id}/sign — Demander une signature électronique
  - Requis : id, signatories
  - Réponse : 201 — Demande de signature envoyée

## Authentification
ApiKeyAuth — apiKey

---

# document-management-api-v1

**Titre** : Document Management API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
GED v1. DEPRECATED.

## Endpoints
- **GET** /v1/documents — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# document-management-api-v2

**Titre** : Document Management API
**Version** : v2 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Gestion electronique documents. Upload, versioning, recherche et workflow validation.

## Endpoints
- **GET** /v2/documents — Catalogue
  - Réponse : 200 — OK
- **POST** /v2/documents — Uploader
  - Réponse : 200 — OK
- **GET** /v2/documents/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/documents/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/documents/{id} — Archiver
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/documents/{id}/versions — Versions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/documents/{id}/versions — Nouvelle version
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/documents/{id}/workflow — Soumettre validation
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/documents/{id}/workflow — Approuver
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# driver-api-v1

**Titre** : Driver API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion conducteurs v1. DEPRECATED.

## Endpoints
- **GET** /v1/drivers — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# driver-api-v2

**Titre** : Driver API
**Version** : v2 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion conducteurs. Permis, scores de conduite et tachygraphe. DIFFERENCE vs employee-api : Driver = données spécifiques conducteurs (permis, infractions), Employee = données RH génériques.

## Endpoints
- **GET** /v2/drivers — Lister conducteurs
  - Réponse : 200 — OK
- **POST** /v2/drivers — Ajouter conducteur
  - Réponse : 200 — OK
- **GET** /v2/drivers/{id} — Profile conducteur
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/drivers/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/drivers/{id}/license — Permis de conduire
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/drivers/{id}/license — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/drivers/{id}/score — Score de conduite
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# drone-survey-api

**Titre** : Drone Survey API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Relevés par drone. Cartographie NDVI, détection stress et rapports.

## Endpoints
- **GET** /v1/drone-surveys — Relevés planifiés
  - Réponse : 200 — OK
- **POST** /v1/drone-surveys — Planifier relevé
  - Réponse : 200 — OK
- **GET** /v1/drone-surveys/{id} — Indice NDVI
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/drone-surveys/{id}/anomalies — Anomalies cultures
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# drug-interaction-api

**Titre** : Drug Interaction API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Vérification interactions médicamenteuses et contre-indications. DIFFÉRENCE vs prescription-api : Drug Interaction = vérification sécurité avant prescription, Prescription = document légal de dispensation.

## Endpoints
- **POST** /v1/interactions/check — Vérifier interactions
  - Réponse : 200 — OK
- **GET** /v1/interactions/{drugId} — Interactions d'un médicament
  - Requis : drugId
  - Réponse : 200 — OK
- **POST** /v1/contraindications/check — Vérifier contre-indications
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# due-diligence-api

**Titre** : Due Diligence API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Due diligence juridique et financiere. Checklist, documents et rapport final.

## Endpoints
- **GET** /v1/due-diligence — Audits en cours
  - Réponse : 200 — OK
- **POST** /v1/due-diligence — Lancer due diligence
  - Réponse : 200 — OK
- **GET** /v1/due-diligence/{id} — Avancement
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/due-diligence/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/due-diligence/{id}/findings — Findings
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/due-diligence/{id}/findings — Ajouter
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/due-diligence/{id}/report — Rapport final
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# e-discovery-api

**Titre** : E-Discovery API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Decouverte electronique. Collecte, preservation et analyse documents pour litiges.

## Endpoints
- **GET** /v1/ediscovery/holds — Holds actifs
  - Réponse : 200 — OK
- **POST** /v1/ediscovery/holds — Creer hold
  - Réponse : 200 — OK
- **GET** /v1/ediscovery/holds/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/ediscovery/holds/{id} — Lever hold
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/ediscovery/collections/{id} — Collection
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/ediscovery/collections/{id} — Exporter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# email-api

**Titre** : Email API
**Version** : v2 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Envoi d'emails transactionnels et marketing avec templates, tracking et gestion des bounces. Canal email seul. DIFFÉRENCE vs notification-api : Email API se spécialise sur l'email avec templates Handlebars, tracking ouverture/clic, listes de suppression. Notification API orchestre plusieurs canaux sans ces fonctionnalités avancées.

## Endpoints
- **POST** /v2/emails/send — Envoyer un email transactionnel
  - Réponse : 201 — Envoyé | 400 — 
- **POST** /v2/emails/batch — Envoi en masse (max 10 000 destinataires)
  - Réponse : 202 — Traitement asynchrone lancé
- **GET** /v2/emails/{id}/status — Statut de livraison d'un email
  - Requis : id
  - Réponse : 200 — Statut
- **GET** /v2/emails/templates — Lister les templates email
  - Réponse : 200 — Templates
- **POST** /v2/emails/templates — Créer un template email (Handlebars)
  - Réponse : 201 — Créé
- **GET** /v2/emails/suppressions — Lister les adresses supprimées (bounces, unsubscribes)
  - Réponse : 200 — Suppressions

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# emergency-api

**Titre** : Emergency API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Gestion des urgences médicales. Triage CCMU, passages aux urgences et orientation services.

## Endpoints
- **GET** /v1/emergency/triage — File de triage
  - Réponse : 200 — OK
- **POST** /v1/emergency/triage — Enregistrer triage
  - Réponse : 200 — OK
- **GET** /v1/emergency/cases — Cas en cours
  - Réponse : 200 — OK
- **POST** /v1/emergency/cases — Ouvrir cas urgence
  - Réponse : 200 — OK
- **GET** /v1/emergency/cases/{id} — Détail cas
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/emergency/cases/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/emergency/cases/{id} — Clore
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# employee-api

**Titre** : Employee API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Dossiers RH des collaborateurs internes : contrats, paie, congés, évaluations. DIFFÉRENCE vs user-api : Employee = données RH sensibles (salaire, contrat). User = credentials. DIFFÉRENCE vs customer-profile-api : Employee = collaborateur interne, Customer = acheteur externe. DIFFÉRENCE vs account-api : Employee = personne physique interne, Account = organisation cliente. Accès restreint scope hr:read/write.

## Endpoints
- **GET** /v1/employees — Lister les employés
  - Réponse : 200 — Liste
- **POST** /v1/employees — Créer un dossier employé (onboarding)
  - Réponse : 201 — Créé
- **GET** /v1/employees/{id} — Fiche employé complète
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/employees/{id} — Modifier le dossier
  - Requis : id
  - Réponse : 200 — Mis à jour
- **GET** /v1/employees/{id}/contracts — Historique des contrats
  - Requis : id
  - Réponse : 200 — Contrats
- **GET** /v1/employees/{id}/leaves — Soldes et historique congés
  - Requis : id
  - Réponse : 200 — Congés
- **GET** /v1/employees/{id}/salary — Informations salariales (accès restreint hr:payroll)
  - Requis : id
  - Réponse : 200 — Salaire | 403 — Scope hr:payroll requis

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# encryption-api

**Titre** : Encryption API
**Version** : v1 | **Statut** : active
**Domaine** : Security & Compliance | **Équipe** : Equipe Security

## Description
Chiffrement et gestion des clés cryptographiques. AES, RSA et gestion de vault.

## Endpoints
- **POST** /v1/encrypt — Chiffrer une donnée
  - Requis : data, key_id
  - Réponse : 200 — Données chiffrées
- **POST** /v1/decrypt — Déchiffrer une donnée
  - Requis : ciphertext, key_id
  - Réponse : 200 — Données déchiffrées
- **POST** /v1/keys — Générer une clé cryptographique
  - Requis : name, type
  - Réponse : 201 — Clé créée
- **GET** /v1/keys — Lister les clés (métadonnées uniquement)
  - Réponse : 200 — Clés
- **POST** /v1/keys/{id}/rotate — Rotation d'une clé cryptographique
  - Requis : id
  - Réponse : 200 — Rotation effectuée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# endorsement-api

**Titre** : Endorsement API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Avenants et modifications de contrats. Ajout garanties, changement données. DIFFERENCE vs policy-api : Endorsement = modification ponctuelle d'un contrat existant, Policy = gestion contrat complet.

## Endpoints
- **GET** /v1/endorsements — Avenants en cours
  - Réponse : 200 — OK
- **POST** /v1/endorsements — Créer avenant
  - Réponse : 200 — OK
- **GET** /v1/endorsements/{id} — Detail avenant
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/endorsements/{id} — Approuver
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/endorsements/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# endpoint-protection-api

**Titre** : Endpoint Protection API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Protection endpoints. EDR, antivirus et gestion des postes.

## Endpoints
- **GET** /v1/endpoints — Endpoints managés
  - Réponse : 200 — OK
- **POST** /v1/endpoints — Enrôler endpoint
  - Réponse : 200 — OK
- **GET** /v1/endpoints/{id} — Statut protection
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/endpoints/{id} — Isoler endpoint
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/endpoints/{id}/threats — Menaces détectées
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/endpoints/{id}/threats — Mettre en quarantaine
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# energy-audit-api

**Titre** : Energy Audit API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Audits énergétiques bâtiments. DPE, recommandations et suivi travaux. DIFFERENCE vs carbon-footprint-api : Energy Audit = diagnostic bâtiment DPE, Carbon Footprint = bilan carbone activités.

## Endpoints
- **GET** /v1/audits — Audits réalisés
  - Réponse : 200 — OK
- **POST** /v1/audits — Commander audit
  - Réponse : 200 — OK
- **GET** /v1/audits/{id} — Rapport DPE
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/audits/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/audits/{id}/recommendations — Recommandations travaux
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# energy-consumption-api

**Titre** : Energy Consumption API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Consommation énergétique bâtiments et installations. Courbes de charge et optimisation.

## Endpoints
- **GET** /v1/consumption/{siteId} — Consommation actuelle
  - Requis : siteId
  - Réponse : 200 — OK
- **POST** /v1/consumption/{siteId} — Enregistrer
  - Requis : siteId
  - Réponse : 200 — OK
- **GET** /v1/consumption/{siteId}/history — Historique
  - Requis : siteId
  - Réponse : 200 — OK
- **GET** /v1/consumption/{siteId}/forecast — Prévisions consommation
  - Requis : siteId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# energy-forecast-api

**Titre** : Energy Forecast API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Prévisions consommation énergétique. Modèles ML et courbes de charge. DIFFERENCE vs energy-consumption-api : Forecast = prévisions futures, Consumption = données historiques.

## Endpoints
- **GET** /v1/forecast/{siteId} — Prévisions 24h/7j
  - Requis : siteId
  - Réponse : 200 — OK
- **POST** /v1/forecast/{siteId} — Calculer prévision
  - Requis : siteId
  - Réponse : 200 — OK
- **GET** /v1/forecast/{siteId}/accuracy — Précision modèle
  - Requis : siteId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# energy-industry-api

**Titre** : Energy Industry API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Energie process industriels. Consommation par machine et optimisation. DIFFERENCE vs energy-consumption-api : Energy Industry = energie machines de production, Energy Consumption = batiments et installations.

## Endpoints
- **GET** /v1/energy-industry/{machineId} — Energie par piece
  - Requis : machineId
  - Réponse : 200 — OK
- **GET** /v1/energy-industry/site — Recommandations optimisation
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# enrollment-api-v1

**Titre** : Enrollment API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Inscriptions v1. DEPRECATED.

## Endpoints
- **GET** /v1/enrollments — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# enrollment-api-v2

**Titre** : Enrollment API
**Version** : v2 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Inscriptions cours et programmes. Validation prérequis et listes d'attente.

## Endpoints
- **GET** /v2/enrollments — Lister inscriptions
  - Réponse : 200 — OK
- **POST** /v2/enrollments — S'inscrire
  - Réponse : 200 — OK
- **GET** /v2/enrollments/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/enrollments/{id} — Annuler inscription
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/enrollments/{id}/progress — Progression
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# erp-integration-api

**Titre** : ERP Integration API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Integration ERP SAP/Oracle. Synchronisation donnees et transactions.

## Endpoints
- **POST** /v1/erp/sync — Synchroniser donnees referentielles
  - Réponse : 200 — OK
- **GET** /v1/erp/sync — Statut synchronisation
  - Réponse : 200 — OK
- **GET** /v1/erp/purchase-orders — Commandes achat ERP
  - Réponse : 200 — OK
- **POST** /v1/erp/purchase-orders — Creer commande achat
  - Réponse : 200 — OK
- **GET** /v1/erp/invoices — Factures ERP
  - Réponse : 200 — OK
- **POST** /v1/erp/invoices — Comptabiliser facture
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# escrow-api

**Titre** : Escrow API
**Version** : v1 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Paiements sous séquestre pour marketplaces. Fonds retenus jusqu'à confirmation de livraison, puis libérés.

## Endpoints
- **POST** /v1/escrow — Créer un compte séquestre
  - Requis : order_id, amount, seller_id
  - Réponse : 201 — Séquestre créé
- **GET** /v1/escrow/{id} — Statut du séquestre
  - Requis : id
  - Réponse : 200 — Séquestre | 404 — 
- **POST** /v1/escrow/{id}/release — Libérer les fonds vers le vendeur
  - Requis : id
  - Réponse : 200 — Fonds libérés
- **POST** /v1/escrow/{id}/refund — Rembourser l'acheteur (litige)
  - Requis : id
  - Réponse : 200 — Remboursé

## Authentification
ApiKeyAuth — apiKey

---

# escrow-real-estate-api

**Titre** : Escrow Real Estate API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Séquestre immobilier. Consignation des fonds, conditions et libération. DIFFERENCE vs escrow-api (e-commerce) : Escrow Real Estate = séquestre transactions immobilières, Escrow = séquestre e-commerce.

## Endpoints
- **GET** /v1/escrow/real-estate — Séquestres en cours
  - Réponse : 200 — OK
- **POST** /v1/escrow/real-estate — Créer séquestre
  - Réponse : 200 — OK
- **GET** /v1/escrow/real-estate/{id} — Detail séquestre
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/escrow/real-estate/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# esignature-api

**Titre** : E-Signature API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Signature electronique qualifiee eIDAS. Workflows multi-signataires et archivage probatoire.

## Endpoints
- **GET** /v1/esign/documents — Documents a signer
  - Réponse : 200 — OK
- **POST** /v1/esign/documents — Preparer signature
  - Réponse : 200 — OK
- **GET** /v1/esign/documents/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/esign/documents/{id} — Envoyer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/esign/documents/{id}/signers — Statut signatures
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/esign/documents/{id}/signers — Ajouter signataire
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/esign/documents/{id}/archive — Archiver
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# esim-api

**Titre** : eSIM API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Gestion eSIM. Profils, activation et transfert.

## Endpoints
- **GET** /v1/esim/{deviceId} — Profils
  - Requis : deviceId
  - Réponse : 200 — OK
- **POST** /v1/esim/{deviceId} — Activer
  - Requis : deviceId
  - Réponse : 200 — OK
- **POST** /v1/esim/{deviceId}/transfer — Transferer
  - Requis : deviceId
  - Réponse : 200 — OK
- **GET** /v1/esim/qrcode/{profileId} — QR code
  - Requis : profileId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# eta-api

**Titre** : ETA API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Calcul temps d'arrivée estimé. Trafic temps réel, conditions météo et historique. DIFFERENCE vs route-optimization-api : ETA = estimation heure arrivee, Route = calcul itineraire optimal.

## Endpoints
- **POST** /v1/eta/calculate — Calculer ETA
  - Réponse : 200 — OK
- **GET** /v1/eta/{shipmentId} — ETA livraison
  - Requis : shipmentId
  - Réponse : 200 — OK
- **PUT** /v1/eta/{shipmentId} — Mettre a jour ETA
  - Requis : shipmentId
  - Réponse : 200 — OK
- **GET** /v1/eta/history/{routeId} — Précision historique ETA
  - Requis : routeId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# etl-api

**Titre** : ETL API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Extract Transform Load. Jobs, transformations et chargement.

## Endpoints
- **GET** /v1/etl/jobs — Jobs
  - Réponse : 200 — OK
- **POST** /v1/etl/jobs — Creer
  - Réponse : 200 — OK
- **GET** /v1/etl/jobs/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/etl/jobs/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/etl/jobs/{id} — Executer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/etl/jobs/{id}/runs/{runId} — Logs
  - Requis : id, runId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# ev-charging-api-v1

**Titre** : EV Charging API
**Version** : v1 | **Statut** : deprecated
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Bornes recharge vehicules electriques v1. DEPRECATED.

## Endpoints
- **GET** /v1/stations — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# ev-charging-api-v2

**Titre** : EV Charging API
**Version** : v2 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Bornes recharge VE. Disponibilité temps réel, réservation et facturation. DIFFERENCE vs parking-api : EV Charging = recharge vehicules electriques, Parking = stationnement generique.

## Endpoints
- **GET** /v2/stations — Stations disponibles
  - Réponse : 200 — OK
- **POST** /v2/stations — Enregistrer
  - Réponse : 200 — OK
- **GET** /v2/stations/{id} — Disponibilite
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/stations/{id}/session — Démarrer recharge
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/stations/{id}/session — Arreter
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/stations/{id}/history — Historique recharges
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# event-api

**Titre** : Event API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Gestion des événements métier publiés sur le bus d'événements (Event Bus). Publication, souscription et replay. DIFFÉRENCE vs event-tracking-api : Event API est le bus d'événements système (ordre.créé, paiement.réussi) pour la communication entre microservices, Event Tracking API collecte les événements comportementaux utilisateurs pour l'analytics. DIFFÉRENCE vs calendar-api : Event API = événements systèmes asynchrones, Calendar API = événements humains planifiés dans le temps.

## Endpoints
- **POST** /v1/events/publish — Publier un événement sur le bus
  - Réponse : 202 — Événement publié
- **POST** /v1/events/subscriptions — Souscrire à un type d'événement
  - Requis : event_type, endpoint_url
  - Réponse : 201 — Souscription créée
- **GET** /v1/events/subscriptions — Lister les souscriptions actives
  - Réponse : 200 — Souscriptions
- **GET** /v1/events — Consulter le journal des événements passés
  - Réponse : 200 — Événements
- **POST** /v1/events/replay — Rejouer des événements passés (utile après incident)
  - Requis : from, to
  - Réponse : 202 — Replay lancé
- **GET** /v1/events/types — Catalogue des types d'événements disponibles
  - Réponse : 200 — Types avec schéma JSON de chaque payload

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# event-bus-api

**Titre** : Event Bus API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Bus d'evenements. Publication, souscription et replay. DIFFERENCE vs streaming-api : Event Bus = evenements metier asynchrones, Streaming = flux donnees haute frequence.

## Endpoints
- **POST** /v1/events — Publier evenement
  - Réponse : 200 — OK
- **GET** /v1/events — Types evenements
  - Réponse : 200 — OK
- **GET** /v1/events/subscriptions — Abonnements
  - Réponse : 200 — OK
- **POST** /v1/events/subscriptions — S'abonner
  - Réponse : 200 — OK
- **POST** /v1/events/replay/{correlationId} — Rejouer evenements
  - Requis : correlationId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# event-tracking-api

**Titre** : Event Tracking API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Collecte d'événements comportementaux utilisateurs. Clics, pages vues, funnels de conversion.

## Endpoints
- **POST** /v1/events/track — Enregistrer un événement utilisateur
  - Requis : event, user_id
  - Réponse : 202 — Enregistré
- **POST** /v1/events/batch — Envoi groupé d'événements
  - Réponse : 202 — Traitement asynchrone
- **GET** /v1/events/funnels/{funnelId} — Analyse d'un funnel de conversion
  - Requis : funnelId
  - Réponse : 200 — Funnel
- **GET** /v1/events/sessions/{userId} — Sessions d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Sessions

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# event-venue-api

**Titre** : Event Venue API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Salles événementielles et lieux réception. Capacité, équipements et tarification. DIFFERENCE vs virtual-classroom-api : Event Venue = lieu physique événementiel, Virtual Classroom = salle de cours en ligne.

## Endpoints
- **GET** /v1/venues — Lieux disponibles
  - Réponse : 200 — OK
- **POST** /v1/venues — Référencer lieu
  - Réponse : 200 — OK
- **GET** /v1/venues/{id} — Disponibilité
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/venues/{id}/bookings — Réservations
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/venues/{id}/bookings — Réserver lieu
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# exam-api

**Titre** : Exam API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Examens officiels. Planification, surveillance et résultats.

## Endpoints
- **GET** /v1/exams — Examens planifiés
  - Réponse : 200 — OK
- **POST** /v1/exams — Créer examen
  - Réponse : 200 — OK
- **GET** /v1/exams/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/exams/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/exams/{id}/candidates — Candidats inscrits
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/exams/{id}/candidates — Inscrire candidat
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/exams/{id}/results — Résultats
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/exams/{id}/results — Publier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# excess-api

**Titre** : Excess API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Franchises et auto-rétentions. Calcul et application lors des sinistres.

## Endpoints
- **GET** /v1/excess/{contractId} — Montant franchise
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/excess/{contractId} — Calculer franchise applicable
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/excess/types — Types de franchises
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# expense-api

**Titre** : Expense API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe Finance

## Description
Notes de frais et remboursements employés. Soumission, validation et virement.

## Endpoints
- **POST** /v1/expenses — Soumettre une note de frais
  - Réponse : 201 — Soumise
- **GET** /v1/expenses — Lister les notes de frais
  - Réponse : 200 — Notes de frais
- **GET** /v1/expenses/{id} — Détails d'une note de frais
  - Requis : id
  - Réponse : 200 — Note de frais
- **PUT** /v1/expenses/{id}/approve — Approuver
  - Requis : id
  - Réponse : 200 — Approuvée
- **PUT** /v1/expenses/{id}/reject — Rejeter
  - Requis : id, reason
  - Réponse : 200 — Rejetée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# experiment-tracking-api

**Titre** : Experiment Tracking API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Suivi experiences ML. Runs, metriques et comparaison.

## Endpoints
- **GET** /v1/experiments — Experiences
  - Réponse : 200 — OK
- **POST** /v1/experiments — Creer
  - Réponse : 200 — OK
- **GET** /v1/experiments/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/experiments/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/experiments/{id}/runs — Runs
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/experiments/{id}/runs — Demarrer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/experiments/{id}/runs/{runId}/metrics — Metriques
  - Requis : id, runId
  - Réponse : 200 — OK
- **POST** /v1/experiments/{id}/runs/{runId}/metrics — Logger
  - Requis : id, runId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# farm-equipment-api

**Titre** : Farm Equipment API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Gestion matériel agricole. Tracteurs, machines et maintenance.

## Endpoints
- **GET** /v1/equipment — Matériel agricole
  - Réponse : 200 — OK
- **POST** /v1/equipment — Enregistrer matériel
  - Réponse : 200 — OK
- **GET** /v1/equipment/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/equipment/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/equipment/{id}/maintenance — Maintenance
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/equipment/{id}/maintenance — Planifier entretien
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/equipment/{id}/usage — Utilisation
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# feature-flag-api

**Titre** : Feature Flag API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Feature flags et déploiement progressif (canary, A/B). DIFFÉRENCE vs config-api : Feature Flag = activation/désactivation de fonctionnalités avec rollout progressif et ciblage utilisateurs, Config = paramètres de configuration génériques.

## Endpoints
- **GET** /v1/flags — Lister les feature flags
  - Réponse : 200 — Flags
- **POST** /v1/flags — Créer un feature flag
  - Réponse : 201 — Créé
- **GET** /v1/flags/{key} — Valeur d'un flag pour un contexte utilisateur
  - Requis : key
  - Réponse : 200 — Valeur du flag
- **PUT** /v1/flags/{key} — Mettre à jour un flag
  - Requis : key
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/flags/{key} — Supprimer un flag
  - Requis : key
  - Réponse : 204 — Supprimé
- **PUT** /v1/flags/{key}/rollout — Ajuster le pourcentage de rollout
  - Requis : key, percent
  - Réponse : 200 — Rollout mis à jour

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# feature-store-api

**Titre** : Feature Store API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Registre features ML. Creation, versioning et serving.

## Endpoints
- **GET** /v1/features — Features
  - Réponse : 200 — OK
- **POST** /v1/features — Creer
  - Réponse : 200 — OK
- **GET** /v1/features/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/features/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/features/{id}/versions — Versions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/features/{id}/versions — Publier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/features/serving — Features offline
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fertilizer-api

**Titre** : Fertilizer API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Gestion fertilisants et intrants. Stocks, applications et bilan azoté.

## Endpoints
- **GET** /v1/fertilizers — Fertilisants disponibles
  - Réponse : 200 — OK
- **POST** /v1/fertilizers — Ajouter produit
  - Réponse : 200 — OK
- **GET** /v1/fertilizers/{fieldId}/application — Applications
  - Requis : fieldId
  - Réponse : 200 — OK
- **POST** /v1/fertilizers/{fieldId}/application — Enregistrer application
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v1/fertilizers/{fieldId}/balance — Bilan azoté
  - Requis : fieldId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# field-api-v1

**Titre** : Field API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Parcelles agricoles v1. DEPRECATED.

## Endpoints
- **GET** /v1/fields — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# field-api-v2

**Titre** : Field API
**Version** : v2 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Gestion parcelles agricoles. Cartographie, sol et historique cultural.

## Endpoints
- **GET** /v2/fields — Lister parcelles
  - Réponse : 200 — OK
- **POST** /v2/fields — Créer parcelle
  - Réponse : 200 — OK
- **GET** /v2/fields/{id} — Detail parcelle
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/fields/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/fields/{id}/soil — Données sol
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/fields/{id}/soil — Ajouter analyse
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/fields/{id}/history — Historique cultural
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# file-storage-api

**Titre** : File Storage API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Stockage de fichiers. Upload, téléchargement et organisation. DIFFÉRENCE vs media-api : File Storage = tous types de fichiers (docs, données), Media API = images/vidéos avec traitement (resize, CDN).

## Endpoints
- **POST** /v1/files/upload — Uploader un fichier
  - Réponse : 201 — Uploadé
- **GET** /v1/files/{id} — Métadonnées d'un fichier
  - Requis : id
  - Réponse : 200 — Fichier
- **DELETE** /v1/files/{id} — Supprimer un fichier
  - Requis : id
  - Réponse : 204 — Supprimé
- **GET** /v1/files/{id}/download — Télécharger un fichier
  - Requis : id
  - Réponse : 200 — Fichier
- **POST** /v1/files/presigned-url — Générer une URL pré-signée (upload direct S3)
  - Requis : filename, content_type
  - Réponse : 200 — URL pré-signée valable expires_in secondes

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# firmware-api

**Titre** : Firmware API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Gestion des mises a jour firmware OTA. Distribution, déploiement progressif et rollback. DIFFERENCE vs device-registry-api : Firmware = MAJ logicielle, Device Registry = inventaire materiel.

## Endpoints
- **GET** /v1/firmware/releases — Releases disponibles
  - Réponse : 200 — OK
- **POST** /v1/firmware/releases — Publier release
  - Réponse : 200 — OK
- **GET** /v1/firmware/releases/{id} — Detail release
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/firmware/deployments — Déploiements en cours
  - Réponse : 200 — OK
- **POST** /v1/firmware/deployments — Lancer déploiement
  - Réponse : 200 — OK
- **GET** /v1/firmware/deployments/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/firmware/deployments/{id} — Rollback
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# flash-sale-api

**Titre** : Flash Sale API
**Version** : v1 | **Statut** : active
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Ventes flash et offres limitees. Compteur, stock dedie et urgence.

## Endpoints
- **GET** /v1/flash-sales — Ventes flash actives
  - Réponse : 200 — OK
- **POST** /v1/flash-sales — Créer vente flash
  - Réponse : 200 — OK
- **GET** /v1/flash-sales/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/flash-sales/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/flash-sales/{id} — Terminer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/flash-sales/{id}/stock — Stock dedie
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/flash-sales/{id}/stock — Réserver article
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fleet-api-v1

**Titre** : Fleet API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion flotte v1. DEPRECATED.

## Endpoints
- **GET** /v1/vehicles — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fleet-api-v2

**Titre** : Fleet API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion flotte v2 avec GPS. DEPRECATED.

## Endpoints
- **GET** /v2/vehicles — Lister
  - Réponse : 200 — OK
- **POST** /v2/vehicles — Ajouter
  - Réponse : 200 — OK
- **GET** /v2/vehicles/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fleet-api-v3

**Titre** : Fleet API
**Version** : v3 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion flotte v3 avec maintenance. DEPRECATED.

## Endpoints
- **GET** /v3/vehicles — Lister
  - Réponse : 200 — OK
- **POST** /v3/vehicles — Ajouter
  - Réponse : 200 — OK
- **GET** /v3/vehicles/{id}/maintenance — Maintenance
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fleet-api-v4

**Titre** : Fleet API
**Version** : v4 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion flotte complète. GPS, maintenance, consommation et conducteurs. DIFFERENCE vs vehicle-api : Fleet = gestion ensemble de la flotte, Vehicle = donnees d'un vehicule individuel.

## Endpoints
- **GET** /v4/vehicles — Lister flotte
  - Réponse : 200 — OK
- **POST** /v4/vehicles — Ajouter vehicule
  - Réponse : 200 — OK
- **GET** /v4/vehicles/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v4/vehicles/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v4/vehicles/{id} — Retirer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v4/vehicles/{id}/location — Position GPS temps reel
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v4/vehicles/{id}/maintenance — Historique maintenance
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v4/vehicles/{id}/maintenance — Planifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v4/vehicles/{id}/fuel — Consommation
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# flight-booking-api

**Titre** : Flight Booking API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Réservation vols. Recherche, sièges et check-in en ligne.

## Endpoints
- **POST** /v1/flights/search — Rechercher vols
  - Réponse : 200 — OK
- **GET** /v1/flights/{id} — Detail vol
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/flights/{id} — Réserver vol
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/flights/{bookingId}/seat — Plan cabine
  - Requis : bookingId
  - Réponse : 200 — OK
- **POST** /v1/flights/{bookingId}/seat — Choisir siège
  - Requis : bookingId
  - Réponse : 200 — OK
- **POST** /v1/flights/{bookingId}/checkin — Check-in en ligne
  - Requis : bookingId
  - Réponse : 200 — OK
- **POST** /v1/flights/{bookingId}/cancel — Annuler vol
  - Requis : bookingId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# food-safety-api

**Titre** : Food Safety API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Securite alimentaire. Conformite HACCP, alertes et retraits produits.

## Endpoints
- **GET** /v1/food-safety/checks — Controles
  - Réponse : 200 — OK
- **POST** /v1/food-safety/checks — Creer controle
  - Réponse : 200 — OK
- **GET** /v1/food-safety/recalls — Retraits actifs
  - Réponse : 200 — OK
- **POST** /v1/food-safety/recalls — Initier retrait
  - Réponse : 200 — OK
- **GET** /v1/food-safety/alerts — Alertes
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# forensics-api

**Titre** : Forensics API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Investigation numérique forensique. Analyse artefacts, mémoire et disques.

## Endpoints
- **GET** /v1/forensics/cases — Dossiers forensique
  - Réponse : 200 — OK
- **POST** /v1/forensics/cases — Ouvrir dossier
  - Réponse : 200 — OK
- **GET** /v1/forensics/cases/{id} — Detail dossier
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/forensics/cases/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/forensics/cases/{id}/artifacts — Artefacts collectés
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/forensics/cases/{id}/artifacts — Ajouter artefact
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/forensics/cases/{id}/report — Rapport forensique
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fraud-claims-api

**Titre** : Fraud Claims API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Détection fraude sinistres. Scoring, signaux d'alerte et investigation. DIFFERENCE vs fraud-detection-api (banque) : Fraud Claims = fraude assurance/sinistres, Fraud Detection = fraude transactions bancaires.

## Endpoints
- **POST** /v1/fraud/claims/score — Scorer sinistre suspect
  - Réponse : 200 — OK
- **GET** /v1/fraud/claims/alerts — Alertes fraude
  - Réponse : 200 — OK
- **PUT** /v1/fraud/claims/alerts — Ouvrir investigation
  - Réponse : 200 — OK
- **GET** /v1/fraud/claims/patterns — Patterns fraude détectés
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fraud-detection-api

**Titre** : Fraud Detection API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Detection fraude temps reel sur transactions. DIFFERENCE vs fraud-claims-api assurance : Fraud Detection = transactions bancaires, Fraud Claims = sinistres assurance.

## Endpoints
- **POST** /v1/fraud/score — Scorer transaction
  - Réponse : 200 — OK
- **GET** /v1/fraud/rules — Regles actives
  - Réponse : 200 — OK
- **POST** /v1/fraud/rules — Ajouter regle
  - Réponse : 200 — OK
- **GET** /v1/fraud/alerts — Alertes fraude
  - Réponse : 200 — OK
- **PUT** /v1/fraud/alerts — Resoudre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fraud-telecom-api

**Titre** : Fraud Telecom API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Fraude telecom. IRSF, SIM swap et appels frauduleux. DIFFERENCE vs fraud-detection-api : Fraud Telecom = usage telecom, Fraud Detection = transactions bancaires.

## Endpoints
- **POST** /v1/fraud-telecom/score — Scorer usage
  - Réponse : 200 — OK
- **GET** /v1/fraud-telecom/sim-swap — Alertes
  - Réponse : 200 — OK
- **POST** /v1/fraud-telecom/sim-swap — Bloquer
  - Réponse : 200 — OK
- **GET** /v1/fraud-telecom/alerts — Alertes
  - Réponse : 200 — OK
- **PUT** /v1/fraud-telecom/alerts — Resoudre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# fuel-management-api

**Titre** : Fuel Management API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion carburant flotte. Consommation, ravitaillement et coûts.

## Endpoints
- **GET** /v1/fuel/{vehicleId} — Niveau carburant
  - Requis : vehicleId
  - Réponse : 200 — OK
- **POST** /v1/fuel/{vehicleId} — Enregistrer ravitaillement
  - Requis : vehicleId
  - Réponse : 200 — OK
- **GET** /v1/fuel/consumption/{fleetId} — Coûts carburant
  - Requis : fleetId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# gdpr-api

**Titre** : GDPR API
**Version** : v1 | **Statut** : active
**Domaine** : Security & Compliance | **Équipe** : Equipe Security

## Description
Conformité RGPD. Droit à l'oubli, portabilité des données et gestion des consentements.

## Endpoints
- **POST** /v1/gdpr/delete-request — Demande de suppression (droit à l'oubli)
  - Requis : user_id
  - Réponse : 202 — Traitement sous 30 jours conformément au RGPD
- **POST** /v1/gdpr/export-request — Demande de portabilité des données
  - Requis : user_id
  - Réponse : 202 — Export préparé — lien envoyé par email
- **GET** /v1/gdpr/consents/{userId} — Consentements d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Consentements
- **PUT** /v1/gdpr/consents/{userId} — Mettre à jour les consentements
  - Requis : userId
  - Réponse : 200 — Mis à jour
- **GET** /v1/gdpr/requests/{id}/status — Statut d'une demande RGPD
  - Requis : id
  - Réponse : 200 — Statut

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# geolocation-api

**Titre** : Geolocation API
**Version** : v1 | **Statut** : active
**Domaine** : Localisation | **Équipe** : Equipe Platform

## Description
Géolocalisation et cartographie. Geocodage, distances et zones de livraison. DIFFÉRENCE vs localization-api : Geolocation = coordonnées et cartes, Localization = traductions et formats culturels.

## Endpoints
- **POST** /v1/geo/geocode — Convertir une adresse en coordonnées
  - Requis : address
  - Réponse : 200 — Coordonnées lat/lng
- **POST** /v1/geo/reverse-geocode — Convertir des coordonnées en adresse
  - Requis : lat, lng
  - Réponse : 200 — Adresse
- **POST** /v1/geo/distance — Calculer la distance entre deux points
  - Requis : origin, destination
  - Réponse : 200 — Distance et durée
- **POST** /v1/geo/delivery-zone — Vérifier si une adresse est dans une zone de livraison
  - Requis : address, zone_id
  - Réponse : 200 — Dans la zone ou non

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# gift-card-api

**Titre** : Gift Card API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Cartes cadeaux et bons d'achat. Émission, activation, utilisation et suivi du solde.

## Endpoints
- **POST** /v1/gift-cards/issue — Émettre une carte cadeau
  - Requis : amount, currency
  - Réponse : 201 — Carte émise avec code unique
- **GET** /v1/gift-cards/{code} — Solde et validité d'une carte cadeau
  - Requis : code
  - Réponse : 200 — Carte | 404 — 
- **POST** /v1/gift-cards/{code}/redeem — Utiliser une carte cadeau pour payer
  - Requis : code, amount, order_id
  - Réponse : 200 — Montant débité | 400 — Solde insuffisant ou carte expirée
- **GET** /v1/gift-cards/{code}/balance-history — Historique des utilisations
  - Requis : code
  - Réponse : 200 — Historique

## Authentification
ApiKeyAuth — apiKey

---

# grade-api-v1

**Titre** : Grade API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Notes v1. DEPRECATED.

## Endpoints
- **GET** /v1/grades — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# grade-api-v2

**Titre** : Grade API
**Version** : v2 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Notes et évaluations. Saisie, calcul moyennes et bulletins.

## Endpoints
- **GET** /v2/grades/{studentId} — Notes étudiant
  - Requis : studentId
  - Réponse : 200 — OK
- **POST** /v2/grades/{studentId} — Ajouter note
  - Requis : studentId
  - Réponse : 200 — OK
- **GET** /v2/grades/{studentId}/average — Moyenne générale
  - Requis : studentId
  - Réponse : 200 — OK
- **GET** /v2/grades/{studentId}/report-card — Bulletin de notes
  - Requis : studentId
  - Réponse : 200 — OK
- **POST** /v2/grades/{studentId}/report-card — Générer bulletin
  - Requis : studentId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# grid-api

**Titre** : Grid API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Gestion réseau électrique intelligent. Flux de puissance, équilibrage et incidents.

## Endpoints
- **GET** /v1/grid/status — Statut réseau
  - Réponse : 200 — OK
- **GET** /v1/grid/nodes — Noeuds du réseau
  - Réponse : 200 — OK
- **POST** /v1/grid/nodes — Ajouter noeud
  - Réponse : 200 — OK
- **GET** /v1/grid/nodes/{id} — Detail noeud
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/grid/nodes/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/grid/incidents — Incidents en cours
  - Réponse : 200 — OK
- **POST** /v1/grid/incidents — Signaler
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# grid-stability-api

**Titre** : Grid Stability API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Stabilité et équilibrage du réseau électrique. Fréquence, tension et prédictions. DIFFERENCE vs grid-api : Grid Stability = analyse stabilité et prédictions, Grid = gestion noeuds et incidents.

## Endpoints
- **GET** /v1/stability/status — Statut stabilité réseau
  - Réponse : 200 — OK
- **GET** /v1/stability/frequency — Historique fréquence
  - Réponse : 200 — OK
- **GET** /v1/stability/forecast — Prévisions stabilité
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# harvest-api

**Titre** : Harvest API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Planification et suivi des récoltes. Dates optimales, équipements et tonnages.

## Endpoints
- **GET** /v1/harvests — Récoltes planifiées
  - Réponse : 200 — OK
- **POST** /v1/harvests — Planifier récolte
  - Réponse : 200 — OK
- **GET** /v1/harvests/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/harvests/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/harvests/{id} — Terminer récolte
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/harvests/{id}/tonnage — Tonnage récolté
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/harvests/{id}/tonnage — Enregistrer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# health-api

**Titre** : Health Check API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Monitoring de la santé des services. Status, disponibilité et métriques de performance.

## Endpoints
- **GET** /v1/health — Statut global de la plateforme
  - Réponse : 200 — Tout OK | 503 — Service(s) dégradé(s)
- **GET** /v1/health/services — Statut de chaque microservice
  - Réponse : 200 — Statuts
- **GET** /v1/health/dependencies — Dépendances externes (DB, cache, APIs)
  - Réponse : 200 — Dépendances
- **GET** /v1/health/metrics — Métriques de performance en temps réel
  - Réponse : 200 — Métriques

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# health-check-api

**Titre** : Health Check API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Supervision etat des services. Ping, liveness, readiness et dependances.

## Endpoints
- **GET** /v1/health — Etat global
  - Réponse : 200 — OK
- **GET** /v1/health/services — Etat services
  - Réponse : 200 — OK
- **POST** /v1/health/services — Enregistrer service
  - Réponse : 200 — OK
- **GET** /v1/health/services/{id} — Detail service
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/health/services/{id} — Lancer verification
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# health-insurance-api

**Titre** : Health Insurance API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Assurance santé. Contrats, remboursements et réseaux soins. DIFFERENCE vs insurance-eligibility-api : Health Insurance = gestion contrats côté assureur, Insurance Eligibility = vérification droits côté soignant.

## Endpoints
- **GET** /v1/health-insurance/{contractId} — Contrat sante
  - Requis : contractId
  - Réponse : 200 — OK
- **PUT** /v1/health-insurance/{contractId} — Modifier
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/health-insurance/{contractId}/coverage — Garanties
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/health-insurance/{contractId}/reimbursements — Remboursements
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/health-insurance/{contractId}/reimbursements — Soumettre
  - Requis : contractId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# health-monitoring-api

**Titre** : Health Monitoring API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Monitoring continu patients hospitalisés. Agrégation capteurs IoT médicaux et alertes temps réel.

## Endpoints
- **GET** /v1/monitoring/{patientId} — Données monitoring
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/monitoring/{patientId} — Configurer
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/monitoring/alerts — Alertes actives
  - Réponse : 200 — OK
- **PUT** /v1/monitoring/alerts — Acquitter
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# homeowner-association-api

**Titre** : Homeowner Association API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion copropriété. Assemblées générales, charges et travaux.

## Endpoints
- **GET** /v1/hoa/{buildingId} — Info copropriété
  - Requis : buildingId
  - Réponse : 200 — OK
- **GET** /v1/hoa/{buildingId}/meetings — AG planifiées
  - Requis : buildingId
  - Réponse : 200 — OK
- **POST** /v1/hoa/{buildingId}/meetings — Créer AG
  - Requis : buildingId
  - Réponse : 200 — OK
- **GET** /v1/hoa/{buildingId}/charges — Charges copropriété
  - Requis : buildingId
  - Réponse : 200 — OK
- **POST** /v1/hoa/{buildingId}/charges — Appliquer charges
  - Requis : buildingId
  - Réponse : 200 — OK
- **GET** /v1/hoa/{buildingId}/works — Travaux
  - Requis : buildingId
  - Réponse : 200 — OK
- **POST** /v1/hoa/{buildingId}/works — Créer travaux
  - Requis : buildingId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# hospital-bed-api

**Titre** : Hospital Bed API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Capacitaire hospitalier. Disponibilité des lits par service, admissions et taux d'occupation.

## Endpoints
- **GET** /v1/beds — Lits disponibles
  - Réponse : 200 — OK
- **POST** /v1/beds — Admettre dans un lit
  - Réponse : 200 — OK
- **GET** /v1/beds/{bedId} — Statut lit
  - Requis : bedId
  - Réponse : 200 — OK
- **PUT** /v1/beds/{bedId} — Changer statut
  - Requis : bedId
  - Réponse : 200 — OK
- **DELETE** /v1/beds/{bedId} — Libérer
  - Requis : bedId
  - Réponse : 200 — OK
- **GET** /v1/beds/occupancy — Taux d'occupation
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# hotel-api-v1

**Titre** : Hotel API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Hotels v1. DEPRECATED.

## Endpoints
- **GET** /v1/hotels — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# hotel-api-v2

**Titre** : Hotel API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Hotels v2 avec tarifs. DEPRECATED.

## Endpoints
- **GET** /v2/hotels — Lister
  - Réponse : 200 — OK
- **POST** /v2/hotels — Ajouter
  - Réponse : 200 — OK
- **GET** /v2/hotels/{id}/rates — Tarifs
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# hotel-api-v3

**Titre** : Hotel API
**Version** : v3 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Gestion hotels complète. Chambres, tarifs dynamiques, services et avis. DIFFERENCE vs co-living-api : Hotel = hébergement touristique court séjour, Co-living = résidence longue durée.

## Endpoints
- **GET** /v3/hotels — Catalogue hotels
  - Réponse : 200 — OK
- **POST** /v3/hotels — Référencer hotel
  - Réponse : 200 — OK
- **GET** /v3/hotels/{id} — Fiche complete
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/hotels/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/hotels/{id}/rooms — Chambres disponibles
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/hotels/{id}/rooms — Ajouter chambre
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/hotels/{id}/rates — Tarifs dynamiques
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/hotels/{id}/rates — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/hotels/{id}/reviews — Avis clients
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# housekeeping-api

**Titre** : Housekeeping API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Gestion ménage hôtelier. Planning, priorités et statut chambres.

## Endpoints
- **GET** /v1/housekeeping/{hotelId} — Plan ménage
  - Requis : hotelId
  - Réponse : 200 — OK
- **POST** /v1/housekeeping/{hotelId} — Créer tâche
  - Requis : hotelId
  - Réponse : 200 — OK
- **GET** /v1/housekeeping/rooms/{roomId} — Statut chambre
  - Requis : roomId
  - Réponse : 200 — OK
- **PUT** /v1/housekeeping/rooms/{roomId} — Changer statut
  - Requis : roomId
  - Réponse : 200 — OK
- **GET** /v1/housekeeping/staff — Equipe ménage
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# hr-api

**Titre** : HR API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
API RH centrale. Organigramme, départements et processus RH.

## Endpoints
- **GET** /v1/hr/employees — Lister les employés
  - Réponse : 200 — Employés
- **POST** /v1/hr/employees — Créer un dossier employé
  - Requis : full_name, email, department, position
  - Réponse : 201 — Créé
- **GET** /v1/hr/org-chart — Organigramme de l'entreprise
  - Réponse : 200 — Organigramme
- **GET** /v1/hr/departments — Liste des départements
  - Réponse : 200 — Départements
- **POST** /v1/hr/departments — Créer un département
  - Requis : name
  - Réponse : 201 — Créé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# hvac-api

**Titre** : HVAC API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Systèmes de chauffage, ventilation et climatisation. Contrôle température et qualité air.

## Endpoints
- **GET** /v1/hvac/{unitId} — Statut HVAC
  - Requis : unitId
  - Réponse : 200 — OK
- **PUT** /v1/hvac/{unitId} — Changer mode
  - Requis : unitId
  - Réponse : 200 — OK
- **GET** /v1/hvac/{unitId}/schedule — Planning
  - Requis : unitId
  - Réponse : 200 — OK
- **PUT** /v1/hvac/{unitId}/schedule — Modifier planning
  - Requis : unitId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# iban-validation-api

**Titre** : IBAN Validation API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Validation IBAN/BIC. DIFFERENCE vs transfer-api : IBAN Validation = verification avant operation, Transfer = execution virement.

## Endpoints
- **POST** /v1/iban/validate — Valider IBAN
  - Réponse : 200 — OK
- **GET** /v1/iban/decode/{iban} — Decoder IBAN
  - Requis : iban
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# identity-governance-api

**Titre** : Identity Governance API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Gouvernance des identités. Cycle de vie, rôles et séparation des tâches. DIFFERENCE vs permission-api : Identity Governance = gouvernance cycle de vie identités, Permission = contrôle accès RBAC.

## Endpoints
- **GET** /v1/identity/governance — Statut gouvernance
  - Réponse : 200 — OK
- **GET** /v1/identity/roles — Rôles
  - Réponse : 200 — OK
- **POST** /v1/identity/roles — Créer rôle
  - Réponse : 200 — OK
- **GET** /v1/identity/sod — Règles séparation tâches
  - Réponse : 200 — OK
- **POST** /v1/identity/sod — Vérifier conflit
  - Réponse : 200 — OK
- **GET** /v1/identity/lifecycle — Cycle de vie
  - Réponse : 200 — OK
- **POST** /v1/identity/lifecycle — Provisionner
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# incoming-inspection-api

**Titre** : Incoming Inspection API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Reception et controle entrants. Controle a reception, echantillonnage et acceptation.

## Endpoints
- **GET** /v1/incoming/{poId} — Controle reception
  - Requis : poId
  - Réponse : 200 — OK
- **POST** /v1/incoming/{poId} — Enregistrer
  - Requis : poId
  - Réponse : 200 — OK
- **GET** /v1/incoming/{poId}/sampling — Plan echantillonnage
  - Requis : poId
  - Réponse : 200 — OK
- **POST** /v1/incoming/{poId}/sampling — Resultat
  - Requis : poId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# inference-api

**Titre** : Inference API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Serving inference ML. DIFFERENCE vs model-registry-api : Inference = execution predictions, Model Registry = gestion versions.

## Endpoints
- **POST** /v1/inference/{modelId} — Prediction
  - Requis : modelId
  - Réponse : 200 — OK
- **GET** /v1/inference/{modelId} — Info modele
  - Requis : modelId
  - Réponse : 200 — OK
- **POST** /v1/inference/batch — Batch
  - Réponse : 200 — OK
- **GET** /v1/inference/batch — Statut
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# insurance-claim-api-v1

**Titre** : Insurance Claim API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Sinistres v1. DEPRECATED.

## Endpoints
- **GET** /v1/claims — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# insurance-claim-api-v2

**Titre** : Insurance Claim API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Sinistres v2 avec documents. DEPRECATED.

## Endpoints
- **GET** /v2/claims — Lister
  - Réponse : 200 — OK
- **POST** /v2/claims — Créer
  - Réponse : 200 — OK
- **POST** /v2/claims/{id}/documents — Uploader
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# insurance-claim-api-v3

**Titre** : Insurance Claim API
**Version** : v3 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Déclaration sinistres complète. Photo, expertise IA et suivi indemnisation. DIFFERENCE vs fraud-claims-api : Claim = sinistre légitime à indemniser, Fraud Claims = sinistre suspect à investiguer.

## Endpoints
- **GET** /v3/claims — Sinistres en cours
  - Réponse : 200 — OK
- **POST** /v3/claims — Déclarer sinistre
  - Réponse : 200 — OK
- **GET** /v3/claims/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/claims/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/claims/{id}/documents — Photos/docs
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/claims/{id}/documents — Documents
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/claims/{id}/assessment — Expertise
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/claims/{id}/assessment — Demander expertise
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/claims/{id}/settlement — Indemnisation
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/claims/{id}/settlement — Approuver
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# insurance-eligibility-api

**Titre** : Insurance Eligibility API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Vérification droits assurance maladie AMO/AMC et calcul reste à charge. DIFFÉRENCE vs health-insurance-api : Insurance Eligibility = vérification droits côté soin, Health Insurance = gestion contrats côté assureur.

## Endpoints
- **POST** /v1/eligibility/check — Vérifier droits ouverts
  - Réponse : 200 — OK
- **GET** /v1/eligibility/{patientId} — Droits du patient
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/eligibility/{patientId}/coverage — Détail couverture
  - Requis : patientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# integration-api

**Titre** : Integration API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Connecteurs vers systèmes tiers. ERP, CRM externes, marketplaces et plateformes partenaires.

## Endpoints
- **GET** /v1/integrations — Lister les intégrations disponibles
  - Réponse : 200 — Intégrations
- **POST** /v1/integrations/{name}/connect — Connecter une intégration
  - Requis : name
  - Réponse : 201 — Connectée
- **DELETE** /v1/integrations/{name}/disconnect — Déconnecter une intégration
  - Requis : name
  - Réponse : 204 — Déconnectée
- **POST** /v1/integrations/{name}/sync — Forcer une synchronisation
  - Requis : name
  - Réponse : 202 — Sync lancée
- **GET** /v1/integrations/{name}/status — Statut de connexion
  - Requis : name
  - Réponse : 200 — Statut

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# intellectual-property-api

**Titre** : Intellectual Property API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Propriete intellectuelle. Brevets, marques, droits d'auteur et litiges.

## Endpoints
- **GET** /v1/ip/assets — Actifs PI
  - Réponse : 200 — OK
- **POST** /v1/ip/assets — Deposer
  - Réponse : 200 — OK
- **GET** /v1/ip/assets/{id} — Detail actif PI
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/ip/assets/{id} — Renouveler
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/ip/assets/{id} — Abandonner
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/ip/assets/{id}/licenses — Licences
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/ip/assets/{id}/licenses — Créer licence
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/ip/search — Rechercher conflits
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# interest-rate-api

**Titre** : Interest Rate API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Taux d'interet (EURIBOR, BCE). Publication et historique.

## Endpoints
- **GET** /v1/rates — Taux actuels
  - Réponse : 200 — OK
- **GET** /v1/rates/{type} — Taux par type
  - Requis : type
  - Réponse : 200 — OK
- **POST** /v1/rates/calculate — Calculer interets
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# intermodal-api

**Titre** : Intermodal API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Transport intermodal. Combinaison modes, ruptures de charge et coordination.

## Endpoints
- **GET** /v1/intermodal/shipments — Envois intermodaux
  - Réponse : 200 — OK
- **POST** /v1/intermodal/shipments — Creer
  - Réponse : 200 — OK
- **GET** /v1/intermodal/shipments/{id} — Statut rupture de charge
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# inventory-api-v1

**Titre** : Inventory API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Version 1 inventaire. DEPRECATED 2021. Pas d'alertes de seuil, pas de réapprovisionnement automatique, pas d'historique mouvements. Migrer vers v3.

## Endpoints
- **GET** /v1/inventory — Inventaire global
  - Réponse : 200 — Inventaire
- **GET** /v1/inventory/{productId} — Stock d'un produit
  - Requis : productId
  - Réponse : 200 — Stock | 404 — 
- **PUT** /v1/inventory/{productId} — Mettre à jour le stock
  - Requis : productId, quantity
  - Réponse : 200 — Mis à jour

## Authentification
ApiKeyAuth — apiKey

---

# inventory-api-v2

**Titre** : Inventory API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Version 2 inventaire — DEPRECATED depuis 2023, migrer vers v3. Introduit les alertes de seuil configurables, l'historique des mouvements et le support multi-entrepôt basique. Incompatible avec v1 (IDs entiers → string ITEM-XXX).

## Endpoints
- **GET** /v2/inventory — Inventaire global avec filtres entrepôt
  - Réponse : 200 — Inventaire
- **GET** /v2/inventory/{itemId} — Stock d'un produit
  - Requis : itemId
  - Réponse : 200 — Stock
- **PUT** /v2/inventory/{itemId} — Mettre à jour le stock (BREAKING v3: remplacé par PATCH /stock)
  - Requis : itemId, quantity, operation
  - Réponse : 200 — Mis à jour
- **GET** /v2/inventory/{itemId}/movements — Historique des mouvements de stock (nouveau en v2)
  - Requis : itemId
  - Réponse : 200 — Mouvements
- **POST** /v2/inventory/alerts — Configurer alerte de seuil bas (nouveau en v2)
  - Requis : item_id, threshold
  - Réponse : 201 — Alerte configurée
- **GET** /v2/inventory/alerts — Lister les alertes configurées
  - Réponse : 200 — Alertes

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# inventory-api

**Titre** : Inventory API
**Version** : v3 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Stocks et inventaires produits en temps réel. Alertes rupture et réapprovisionnement automatique. DIFFÉRENCE vs warehouse-api : Inventory = quantités (combien ?), Warehouse = emplacements physiques (où ?).

## Endpoints
- **GET** /v3/inventory — Inventaire global
  - Réponse : 200 — Inventaire
- **DELETE** /v3/inventory/{productId} — Archiver un produit de l'inventaire
  - Réponse : 204 — Archivé
- **PUT** /v3/inventory/{productId}/stock — Mettre à jour le stock
  - Requis : productId, quantity, operation
  - Réponse : 200 — Mis à jour
- **POST** /v3/inventory/alerts — Configurer une alerte de rupture
  - Requis : product_id, threshold
  - Réponse : 201 — Alerte configurée
- **POST** /v3/inventory/restock — Déclencher un réapprovisionnement
  - Requis : product_id, quantity
  - Réponse : 202 — Réapprovisionnement lancé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# inventory-industry-api

**Titre** : Inventory Industry API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Stocks industriels. Matieres premieres, composants et produits finis. DIFFERENCE vs inventory-api : Inventory Industry = stocks de production, Inventory = stock retail.

## Endpoints
- **GET** /v1/stock — Articles en stock
  - Réponse : 200 — OK
- **POST** /v1/stock — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/stock/{id} — Niveau stock
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/stock/{id} — Ajuster stock
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/stock/movements — Mouvements
  - Réponse : 200 — OK
- **POST** /v1/stock/movements — Enregistrer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# inventory-telecom-api

**Titre** : Inventory Telecom API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Inventaire SIM, equipements et materiel. Stock et affectation. DIFFERENCE vs inventory-api : Inventory Telecom = SIM/equipements reseau, Inventory = produits retail.

## Endpoints
- **GET** /v1/inventory-telecom/sim — Stock SIM
  - Réponse : 200 — OK
- **POST** /v1/inventory-telecom/sim — Ajouter SIM
  - Réponse : 200 — OK
- **GET** /v1/inventory-telecom/equipment — Equipements
  - Réponse : 200 — OK
- **POST** /v1/inventory-telecom/equipment — Affecter
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# investment-api

**Titre** : Investment API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Placements financiers OPCVM, ETF, obligations. Catalogue produits et passation ordres. DIFFERENCE vs portfolio-api : Investment = passation ordres et catalogue, Portfolio = analyse portefeuille existant.

## Endpoints
- **GET** /v1/investments/{clientId} — Portefeuille client
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/investments/products — Catalogue produits
  - Réponse : 200 — OK
- **GET** /v1/investments/orders — Ordres en cours
  - Réponse : 200 — OK
- **POST** /v1/investments/orders — Passer ordre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# invoice-api-v2

**Titre** : Invoice API
**Version** : v2 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version 2 de la facture. Ajout des avoirs (credit notes), facturation en plusieurs langues et signature électronique. DIFFÉRENCE vs v1 : credit_note automatique à l'annulation, multi-devises natif, signature eIDAS.

## Endpoints
- **POST** /v2/invoices — Générer une facture multilingue et multi-devise
  - Réponse : 201 — Facture générée
- **GET** /v2/invoices/{id} — Récupérer une facture
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **GET** /v2/invoices/{id}/pdf — PDF facture dans la langue configurée
  - Requis : id
  - Réponse : 200 — PDF
- **PUT** /v2/invoices/{id}/void — Annuler (génère automatiquement un avoir/credit_note)
  - Requis : id
  - Réponse : 200 — Annulée — credit_note générée automatiquement
- **GET** /v2/invoices/{id}/credit-notes — Avoirs liés à cette facture
  - Requis : id
  - Réponse : 200 — Avoirs
- **POST** /v2/invoices/{id}/sign — Signer électroniquement (eIDAS)
  - Requis : id
  - Réponse : 200 — Signée — signature_url disponible

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# invoice-api-v3

**Titre** : Invoice API
**Version** : v3 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version 3 de l'API facture — version actuelle recommandée. Ajout de la facturation récurrente native, des pénalités de retard automatiques et de l'intégration comptable (exports FEC, DATEV). DIFFÉRENCE vs billing-api : Invoice génère et archive les documents fiscaux légaux, Billing orchestre les prélèvements automatiques.

## Endpoints
- **POST** /v3/invoices — Générer facture avec récurrence et export comptable
  - Réponse : 201 — Facture générée | 402 — Paiement requis pour activation récurrence
- **GET** /v3/invoices — Lister factures avec filtres avancés
  - Réponse : 200 — Factures
- **GET** /v3/invoices/{id} — Facture complète avec statut pénalité
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **GET** /v3/invoices/{id}/pdf — PDF multilingue, signé eIDAS si B2B > 10k€
  - Requis : id
  - Réponse : 200 — PDF
- **GET** /v3/invoices/{id}/accounting-export — Export comptable (FEC / DATEV / SAGE / CEGID) — nouveau en v3
  - Requis : id, format
  - Réponse : 200 — Fichier comptable
- **POST** /v3/invoices/{id}/penalty — Appliquer manuellement une pénalité de retard
  - Requis : id
  - Réponse : 200 — Pénalité appliquée et facture mise à jour
- **PUT** /v3/invoices/{id}/void — Annuler (génère avoir + pénalité réversée si applicable)
  - Requis : id
  - Réponse : 200 — Annulée — avoir généré

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# invoice-api

**Titre** : Invoice API
**Version** : v1 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Génération de documents de facturation conformes. Factures, avoirs, notes de débit en PDF. DIFFÉRENCE vs payment-api : Invoice = document fiscal APRÈS paiement, Payment = transaction. DIFFÉRENCE vs billing-api : Invoice = PDFs envoyés aux clients, Billing = prélèvements automatiques. Cas d'usage : facture après commande payée, avoir après remboursement.

## Endpoints
- **POST** /v1/invoices — Générer une facture
  - Réponse : 201 — Générée
- **GET** /v1/invoices/{id} — Récupérer une facture
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **GET** /v1/invoices/{id}/pdf — Télécharger en PDF
  - Requis : id
  - Réponse : 200 — PDF
- **POST** /v1/invoices/{id}/send — Envoyer par email au client
  - Requis : id
  - Réponse : 200 — Envoyée
- **PUT** /v1/invoices/{id}/void — Annuler une facture (génère un avoir automatiquement)
  - Requis : id
  - Réponse : 200 — Annulée — avoir généré

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# irrigation-api-v1

**Titre** : Irrigation API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Irrigation v1. DEPRECATED.

## Endpoints
- **GET** /v1/irrigation — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# irrigation-api-v2

**Titre** : Irrigation API
**Version** : v2 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Gestion systèmes d'irrigation. Programmation, consommation eau et optimisation.

## Endpoints
- **GET** /v2/irrigation/{fieldId} — Statut irrigation
  - Requis : fieldId
  - Réponse : 200 — OK
- **POST** /v2/irrigation/{fieldId} — Arrêter
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v2/irrigation/{fieldId}/schedule — Planning
  - Requis : fieldId
  - Réponse : 200 — OK
- **PUT** /v2/irrigation/{fieldId}/schedule — Modifier
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v2/irrigation/{fieldId}/consumption — Consommation eau
  - Requis : fieldId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# key-rotation-api

**Titre** : Key Rotation API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Rotation clés cryptographiques. HSM, KMS et politiques rotation. DIFFERENCE vs certificate-management-api : Key Rotation = clés symétriques/asymétriques KMS, Certificate Management = certificats X.509 publics.

## Endpoints
- **GET** /v1/keys — Clés cryptographiques
  - Réponse : 200 — OK
- **POST** /v1/keys — Créer clé
  - Réponse : 200 — OK
- **GET** /v1/keys/{id} — Info clé
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/keys/{id} — Rotation manuelle
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/keys/{id} — Désactiver
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/keys/rotation-policy — Politique rotation
  - Réponse : 200 — OK
- **PUT** /v1/keys/rotation-policy — Mettre a jour
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# knowledge-base-api

**Titre** : Knowledge Base API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Base de connaissances et FAQ. Articles, recherche sémantique et suggestions automatiques.

## Endpoints
- **GET** /v1/kb/articles — Lister les articles
  - Réponse : 200 — Articles
- **POST** /v1/kb/articles — Créer un article
  - Requis : title, content, category
  - Réponse : 201 — Créé
- **GET** /v1/kb/articles/{id} — Lire un article
  - Requis : id
  - Réponse : 200 — Article
- **GET** /v1/kb/search — Rechercher dans la base de connaissances
  - Requis : q
  - Réponse : 200 — Résultats
- **GET** /v1/kb/suggest — Suggestions automatiques basées sur un ticket
  - Requis : ticketId
  - Réponse : 200 — Articles suggérés

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# knowledge-graph-api

**Titre** : Knowledge Graph API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Graphe de connaissances. Entites, relations et requetes SPARQL/Cypher.

## Endpoints
- **GET** /v1/kg/entities — Entites
  - Réponse : 200 — OK
- **POST** /v1/kg/entities — Ajouter entite
  - Réponse : 200 — OK
- **GET** /v1/kg/relations — Relations
  - Réponse : 200 — OK
- **POST** /v1/kg/relations — Ajouter relation
  - Réponse : 200 — OK
- **POST** /v1/kg/query — Requeter graphe
  - Réponse : 200 — OK
- **GET** /v1/kg/query — Voisins entite
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# kyc-api-v1

**Titre** : KYC API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
KYC version 1. DEPRECATED.

## Endpoints
- **POST** /v1/kyc — Soumettre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# kyc-api-v2

**Titre** : KYC API
**Version** : v2 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Verification identite KYC/AML avec biometrie et scoring LCB-FT. DIFFERENCE vs aml-api : KYC = verification identite onboarding, AML = surveillance continue transactions.

## Endpoints
- **GET** /v2/kyc/{clientId} — Statut KYC
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v2/kyc/{clientId} — Initier
  - Requis : clientId
  - Réponse : 200 — OK
- **PUT** /v2/kyc/{clientId} — Mettre a jour
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v2/kyc/{clientId}/documents — Soumettre document
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v2/kyc/{clientId}/biometric — Soumettre biometrie
  - Requis : clientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# lab-result-api

**Titre** : Lab Result API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Résultats d'analyses biologiques et de laboratoire. DIFFÉRENCE vs vital-signs-api : Lab = analyses biologiques ponctuelles, Vital Signs = constantes physiologiques continues.

## Endpoints
- **GET** /v1/results/{patientId} — Résultats analyses
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/results/{patientId} — Ajouter résultat
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/results/{patientId}/critical — Valeurs critiques
  - Requis : patientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# lead-api

**Titre** : Lead API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe CRM

## Description
Prospects et leads commerciaux. Scoring, qualification et pipeline de vente. DIFFÉRENCE vs crm-contact-api : Lead = prospects non-convertis en clients dans un pipeline de vente, Contact = toutes les relations existantes.

## Endpoints
- **POST** /v1/leads — Créer un lead
  - Réponse : 201 — Créé
- **GET** /v1/leads — Lister les leads
  - Réponse : 200 — Leads
- **GET** /v1/leads/{id} — Détails d'un lead
  - Requis : id
  - Réponse : 200 — Lead
- **PUT** /v1/leads/{id}/qualify — Qualifier un lead
  - Requis : id, stage
  - Réponse : 200 — Qualifié
- **PUT** /v1/leads/{id}/assign — Assigner à un commercial
  - Requis : id, user_id
  - Réponse : 200 — Assigné
- **GET** /v1/leads/score/{id} — Score de qualification (0-100)
  - Requis : id
  - Réponse : 200 — Score

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# learning-path-api

**Titre** : Learning Path API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Parcours d'apprentissage personnalisés. Recommandations IA et progression adaptative.

## Endpoints
- **GET** /v1/learning-paths — Parcours disponibles
  - Réponse : 200 — OK
- **POST** /v1/learning-paths — Créer parcours
  - Réponse : 200 — OK
- **GET** /v1/learning-paths/{id} — Detail parcours
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/learning-paths/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/learning-paths/recommend/{studentId} — Parcours recommandés
  - Requis : studentId
  - Réponse : 200 — OK
- **GET** /v1/learning-paths/{id}/progress/{studentId} — Progression
  - Requis : id, studentId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# lease-api-v1

**Titre** : Lease API
**Version** : v1 | **Statut** : deprecated
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Contrats de bail v1. DEPRECATED.

## Endpoints
- **GET** /v1/leases — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# lease-api-v2

**Titre** : Lease API
**Version** : v2 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Contrats de bail résidentiels et commerciaux. Indexation, révision et résiliation. DIFFERENCE vs property-api : Lease = contrat juridique de location, Property = bien immobilier.

## Endpoints
- **GET** /v2/leases — Lister baux
  - Réponse : 200 — OK
- **POST** /v2/leases — Créer bail
  - Réponse : 200 — OK
- **GET** /v2/leases/{id} — Detail bail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/leases/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/leases/{id} — Résilier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/leases/{id}/indexation — Calcul indexation
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/leases/{id}/indexation — Appliquer révision
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/leases/{id}/documents — Documents bail
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# leave-api

**Titre** : Leave API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Congés et absences. Demandes, validations, soldes et calendrier.

## Endpoints
- **POST** /v1/leaves/request — Faire une demande de congé
  - Requis : employee_id, type, start_date, end_date
  - Réponse : 201 — Demande créée
- **GET** /v1/leaves/{employeeId} — Congés d'un employé
  - Requis : employeeId
  - Réponse : 200 — Congés
- **PUT** /v1/leaves/{id}/approve — Approuver une demande de congé
  - Requis : id
  - Réponse : 200 — Approuvé
- **PUT** /v1/leaves/{id}/reject — Rejeter une demande de congé
  - Requis : id, reason
  - Réponse : 200 — Rejeté
- **GET** /v1/leaves/{employeeId}/balance — Solde de congés par type
  - Requis : employeeId
  - Réponse : 200 — Soldes

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# legal-billing-api

**Titre** : Legal Billing API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Facturation cabinet d'avocats. Honoraires, temps passe et notes de frais. DIFFERENCE vs billing-api : Legal Billing = honoraires avocats/notaires (temps passe, forfait), Billing = facturation services generiques.

## Endpoints
- **GET** /v1/legal-billing/matters/{matterId} — Facturation dossier
  - Requis : matterId
  - Réponse : 200 — OK
- **POST** /v1/legal-billing/matters/{matterId} — Saisir temps
  - Requis : matterId
  - Réponse : 200 — OK
- **GET** /v1/legal-billing/invoices — Factures
  - Réponse : 200 — OK
- **POST** /v1/legal-billing/invoices — Générer facture
  - Réponse : 200 — OK
- **GET** /v1/legal-billing/invoices/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/legal-billing/invoices/{id} — Envoyer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# legal-entity-api

**Titre** : Legal Entity API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Gestion entites juridiques. Societes, associations et etablissements. DIFFERENCE vs company-profile-api : Legal Entity = donnees juridiques officielles SIREN/SIRET, Company Profile = profil commercial.

## Endpoints
- **GET** /v1/entities — Entites
  - Réponse : 200 — OK
- **POST** /v1/entities — Créer entite
  - Réponse : 200 — OK
- **GET** /v1/entities/{id} — Detail entite
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/entities/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/entities/{id}/documents — Documents officiels
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/entities/{id}/documents — Ajouter
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/entities/search — Rechercher par SIREN/SIRET
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# legal-notice-api

**Titre** : Legal Notice API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Actes juridiques et mises en demeure. Génération, envoi et suivi.

## Endpoints
- **GET** /v1/notices — Actes envoyés
  - Réponse : 200 — OK
- **POST** /v1/notices — Créer acte
  - Réponse : 200 — OK
- **GET** /v1/notices/{id} — Statut remise
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/notices/{id} — Envoyer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# legal-research-api

**Titre** : Legal Research API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Recherche juridique. Jurisprudence, textes de loi et doctrine.

## Endpoints
- **POST** /v1/legal-research/jurisprudence — Rechercher jurisprudence
  - Réponse : 200 — OK
- **GET** /v1/legal-research/jurisprudence — Décisions recentes
  - Réponse : 200 — OK
- **POST** /v1/legal-research/statutes — Rechercher textes de loi
  - Réponse : 200 — OK
- **GET** /v1/legal-research/statutes — Texte officiel
  - Réponse : 200 — OK
- **POST** /v1/legal-research/doctrine — Rechercher doctrine
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# library-api

**Titre** : Library API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Bibliothèque numérique. Catalogue, emprunts et ressources en ligne.

## Endpoints
- **GET** /v1/library/books — Rechercher
  - Réponse : 200 — OK
- **POST** /v1/library/books — Ajouter ouvrage
  - Réponse : 200 — OK
- **GET** /v1/library/books/{id} — Detail ouvrage
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/library/books/{id} — Retourner
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/library/loans/{studentId} — Emprunts étudiant
  - Requis : studentId
  - Réponse : 200 — OK
- **GET** /v1/library/digital — Ressources numériques
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# life-insurance-api

**Titre** : Life Insurance API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Assurance vie et prévoyance. Contrats, rachats et désignation bénéficiaires.

## Endpoints
- **GET** /v1/life-insurance — Contrats vie
  - Réponse : 200 — OK
- **POST** /v1/life-insurance — Souscrire
  - Réponse : 200 — OK
- **GET** /v1/life-insurance/{contractId} — Detail contrat
  - Requis : contractId
  - Réponse : 200 — OK
- **PUT** /v1/life-insurance/{contractId} — Modifier
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/life-insurance/{contractId}/beneficiaries — Bénéficiaires
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/life-insurance/{contractId}/beneficiaries — Ajouter bénéficiaire
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/life-insurance/{contractId}/surrender — Valeur de rachat
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/life-insurance/{contractId}/surrender — Demander rachat
  - Requis : contractId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# lighting-control-api

**Titre** : Lighting Control API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Contrôle éclairage intelligent bâtiments et voirie. Automatisation et économies d'énergie.

## Endpoints
- **GET** /v1/lighting/zones — Zones éclairage
  - Réponse : 200 — OK
- **POST** /v1/lighting/zones — Ajouter zone
  - Réponse : 200 — OK
- **GET** /v1/lighting/zones/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/lighting/zones/{id} — Planning
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/lighting/scenes — Scènes prédéfinies
  - Réponse : 200 — OK
- **POST** /v1/lighting/scenes — Créer scène
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# litigation-api

**Titre** : Litigation API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Gestion des litiges et contentieux. Dossiers, procedures et suivi judiciaire.

## Endpoints
- **GET** /v1/litigation — Dossiers contentieux
  - Réponse : 200 — OK
- **POST** /v1/litigation — Ouvrir dossier
  - Réponse : 200 — OK
- **GET** /v1/litigation/{id} — Detail dossier
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/litigation/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/litigation/{id}/hearings — Audiences
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/litigation/{id}/hearings — Planifier audience
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/litigation/{id}/documents — Documents
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/litigation/{id}/documents — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# live-chat-api

**Titre** : Live Chat API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Chat en direct avec les agents de support. Sessions, transcriptions et transferts. DIFFÉRENCE vs messaging-api : Live Chat = communication client↔agent support avec files d'attente et SLA, Messaging = chat libre entre utilisateurs. DIFFÉRENCE vs ticket-api : Live Chat = interaction temps réel, Ticket = asynchrone.

## Endpoints
- **POST** /v1/chat/sessions — Démarrer une session de live chat
  - Requis : customer_id
  - Réponse : 201 — Session créée — agent assigné
- **GET** /v1/chat/sessions/{id} — Statut d'une session
  - Requis : id
  - Réponse : 200 — Session
- **POST** /v1/chat/sessions/{id}/messages — Envoyer un message dans la session
  - Requis : id, content
  - Réponse : 201 — Envoyé
- **GET** /v1/chat/sessions/{id}/messages — Historique de la session
  - Requis : id
  - Réponse : 200 — Messages
- **POST** /v1/chat/sessions/{id}/transfer — Transférer vers un autre agent ou département
  - Requis : id
  - Réponse : 200 — Transféré
- **PUT** /v1/chat/sessions/{id}/close — Fermer la session et générer la transcription
  - Requis : id
  - Réponse : 200 — Session fermée — transcription disponible

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# livestock-api-v1

**Titre** : Livestock API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Elevage v1. DEPRECATED.

## Endpoints
- **GET** /v1/livestock — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# livestock-api-v2

**Titre** : Livestock API
**Version** : v2 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Gestion élevage. Identification animaux, santé et traçabilité.

## Endpoints
- **GET** /v2/livestock — Troupeau
  - Réponse : 200 — OK
- **POST** /v2/livestock — Enregistrer animal
  - Réponse : 200 — OK
- **GET** /v2/livestock/{id} — Fiche animal
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/livestock/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/livestock/{id}/health — Suivi santé
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/livestock/{id}/health — Enregistrer événement
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/livestock/{id}/movements — Mouvements
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# lms-integration-api

**Titre** : LMS Integration API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Integration LMS Moodle/Canvas. Sync cours, notes et utilisateurs.

## Endpoints
- **POST** /v1/lms/sync — Synchroniser notes
  - Réponse : 200 — OK
- **GET** /v1/lms/users — Utilisateurs LMS
  - Réponse : 200 — OK
- **POST** /v1/lms/users — Provisionner
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# load-planning-api

**Titre** : Load Planning API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Planification chargement véhicules. Optimisation espace, poids et contraintes.

## Endpoints
- **GET** /v1/loads — Chargements planifiés
  - Réponse : 200 — OK
- **POST** /v1/loads — Créer plan chargement
  - Réponse : 200 — OK
- **GET** /v1/loads/{id} — Plan chargement
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/loads/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/loads/optimize — Optimiser chargement
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# loan-api-v1

**Titre** : Loan API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Prets personnels v1. DEPRECATED.

## Endpoints
- **GET** /v1/loans — Lister
  - Réponse : 200 — OK
- **POST** /v1/loans — Demander
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# loan-api-v2

**Titre** : Loan API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Prets avec scoring. DEPRECATED.

## Endpoints
- **GET** /v2/loans — Lister
  - Réponse : 200 — OK
- **POST** /v2/loans — Demander
  - Réponse : 200 — OK
- **POST** /v2/loans/simulate — Simuler mensualites
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# loan-api-v3

**Titre** : Loan API
**Version** : v3 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Prets personnels et professionnels. Decision IA et echeancier. DIFFERENCE vs mortgage-api : Loan = pret personnel sans garantie, Mortgage = pret immobilier avec hypotheque.

## Endpoints
- **GET** /v3/loans — Portefeuille
  - Réponse : 200 — OK
- **POST** /v3/loans — Demander
  - Réponse : 200 — OK
- **GET** /v3/loans/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/loans/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/loans/{id}/repayments — Echeancier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/loans/{id}/repayments — Rembourser
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/loans/simulate — Simuler
  - Réponse : 200 — OK
- **POST** /v3/loans/{id}/early-repayment — Remboursement anticipe
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# localization-api

**Titre** : Localization API
**Version** : v1 | **Statut** : active
**Domaine** : Localisation | **Équipe** : Equipe Platform

## Description
Traductions et internationalisation. Langues, devises et formats régionaux. DIFFÉRENCE vs geolocation-api : Localization = textes et formats culturels (i18n), Geolocation = coordonnées GPS.

## Endpoints
- **GET** /v1/l10n/translations/{lang} — Toutes les traductions d'une langue
  - Requis : lang
  - Réponse : 200 — Traductions
- **GET** /v1/l10n/currencies — Devises supportées avec taux de change
  - Réponse : 200 — Devises
- **POST** /v1/l10n/translate — Traduire un texte dynamiquement
  - Requis : text, target_lang
  - Réponse : 200 — Texte traduit
- **GET** /v1/l10n/formats/{country} — Formats régionaux (date, nombre, monnaie)
  - Requis : country
  - Réponse : 200 — Formats

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# log-api

**Titre** : Log API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Centralisation et consultation des logs applicatifs. Recherche, filtres et alertes sur patterns.

## Endpoints
- **GET** /v1/logs — Consulter les logs
  - Réponse : 200 — Logs
- **POST** /v1/logs — Publier un log
  - Requis : level, message, service
  - Réponse : 202 — Ingéré
- **GET** /v1/logs/tail/{service} — Logs en temps réel (Server-Sent Events)
  - Requis : service
  - Réponse : 200 — Stream SSE
- **POST** /v1/logs/patterns — Créer une alerte sur un pattern de log
  - Requis : pattern, level
  - Réponse : 201 — Pattern créé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# logistics-tracking-api

**Titre** : Logistics Tracking API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Tracking unifié multi-transporteurs. Agrégation des statuts de tous les transporteurs en une seule API.

## Endpoints
- **GET** /v1/tracking/{code} — Suivi d'un colis par numéro de tracking
  - Requis : code
  - Réponse : 200 — Statut de livraison
- **POST** /v1/tracking/batch — Suivi de plusieurs colis simultanément
  - Requis : tracking_codes
  - Réponse : 200 — Statuts groupés
- **GET** /v1/tracking/{code}/events — Historique complet des événements de livraison
  - Requis : code
  - Réponse : 200 — Événements

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# loyalty-hotel-api

**Titre** : Loyalty Hotel API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Programme fidélité hôtelier. Points, statuts et avantages. DIFFERENCE vs loyalty-points-api : Loyalty Hotel = programme fidélité hôtel (nuitées, upgrades), Loyalty Points = programme fidélité commerce générique.

## Endpoints
- **GET** /v1/loyalty/hotel/{memberId} — Compte fidelite
  - Requis : memberId
  - Réponse : 200 — OK
- **POST** /v1/loyalty/hotel/{memberId} — Gagner points
  - Requis : memberId
  - Réponse : 200 — OK
- **GET** /v1/loyalty/hotel/{memberId}/status — Avantages statut
  - Requis : memberId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# loyalty-points-api

**Titre** : Loyalty Points API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe CRM

## Description
Programme de fidélité. Points accumulés, échangés et historique des récompenses.

## Endpoints
- **GET** /v1/loyalty/{customerId} — Solde de points fidélité
  - Requis : customerId
  - Réponse : 200 — Solde
- **POST** /v1/loyalty/earn — Attribuer des points (après achat)
  - Requis : customer_id, points, order_id
  - Réponse : 200 — Points attribués
- **POST** /v1/loyalty/redeem — Utiliser des points (récompense)
  - Requis : customer_id, points, reward_id
  - Réponse : 200 — Échangés | 400 — Solde insuffisant
- **GET** /v1/loyalty/{customerId}/history — Historique des transactions de fidélité
  - Requis : customerId
  - Réponse : 200 — Historique
- **GET** /v1/loyalty/rewards — Catalogue des récompenses disponibles
  - Réponse : 200 — Récompenses

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# loyalty-points-hotel-api

**Titre** : Loyalty Points Hotel Bridge API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Passerelle points fidelite hotel/retail. Transfert et conversion points. DIFFERENCE vs loyalty-hotel-api : Ce bridge = conversion entre programmes, Loyalty Hotel = programme hotelier direct.

## Endpoints
- **POST** /v1/loyalty-bridge/convert — Convertir retail en hotel
  - Réponse : 200 — OK
- **GET** /v1/loyalty-bridge/rates — Taux de conversion
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# machine-api-v1

**Titre** : Machine API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Machines v1. DEPRECATED.

## Endpoints
- **GET** /v1/machines — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# machine-api-v2

**Titre** : Machine API
**Version** : v2 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Gestion machines industrielles. Etat, capacite et programmes CNC. DIFFERENCE vs device-registry-api : Machine = equipment industriel lourd avec programmes usinage, Device Registry = appareils IoT generiques.

## Endpoints
- **GET** /v2/machines — Machines
  - Réponse : 200 — OK
- **POST** /v2/machines — Ajouter
  - Réponse : 200 — OK
- **GET** /v2/machines/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/machines/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/machines/{id}/status — Etat machine
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/machines/{id}/status — Changer etat
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/machines/{id}/programs — Programmes CNC
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/machines/{id}/programs — Charger programme
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# maintenance-request-api

**Titre** : Maintenance Request API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Demandes d'intervention locataires. Tickets maintenance, priorités et suivi.

## Endpoints
- **GET** /v1/maintenance-requests — Lister demandes
  - Réponse : 200 — OK
- **POST** /v1/maintenance-requests — Créer demande
  - Réponse : 200 — OK
- **GET** /v1/maintenance-requests/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/maintenance-requests/{id} — Mettre a jour statut
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/maintenance-requests/{id} — Affecter technicien
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# maintenance-schedule-api

**Titre** : Maintenance Schedule API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Planification maintenance préventive véhicules. Kilométrage, temps et alertes.

## Endpoints
- **GET** /v1/schedule/{vehicleId} — Planning maintenance
  - Requis : vehicleId
  - Réponse : 200 — OK
- **POST** /v1/schedule/{vehicleId} — Ajouter tache
  - Requis : vehicleId
  - Réponse : 200 — OK
- **GET** /v1/schedule/{vehicleId}/upcoming — Maintenances a venir
  - Requis : vehicleId
  - Réponse : 200 — OK
- **GET** /v1/schedule/alerts — Alertes maintenance
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# maintenance-work-order-api

**Titre** : Maintenance Work Order API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Ordres de travail maintenance. Corrective, preventive et predictive. DIFFERENCE vs maintenance-schedule-api : Maintenance Work Order = OT executes, Maintenance Schedule = planification preventive.

## Endpoints
- **GET** /v1/work-orders — OT en cours
  - Réponse : 200 — OK
- **POST** /v1/work-orders — Creer OT
  - Réponse : 200 — OK
- **GET** /v1/work-orders/{id} — Detail OT
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/work-orders/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/work-orders/{id} — Cloturer OT
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/work-orders/{id}/labor — Main oeuvre
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/work-orders/{id}/labor — Declarer temps
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# media-api

**Titre** : Media API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Médias images et vidéos. Upload, redimensionnement, optimisation et CDN. DIFFÉRENCE vs file-storage-api : Media = traitement multimédia (resize, compress, CDN), File Storage = stockage générique sans traitement.

## Endpoints
- **POST** /v1/media/upload — Uploader un média (image ou vidéo)
  - Réponse : 201 — Uploadé
- **GET** /v1/media/{id} — Métadonnées d'un média
  - Requis : id
  - Réponse : 200 — Média
- **DELETE** /v1/media/{id} — Supprimer un média
  - Requis : id
  - Réponse : 204 — Supprimé
- **POST** /v1/media/{id}/resize — Redimensionner une image
  - Requis : id, width, height
  - Réponse : 200 — Image redimensionnée
- **GET** /v1/media/{id}/cdn-url — URL CDN optimisée d'un média
  - Requis : id
  - Réponse : 200 — URL CDN

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# media-processing-api

**Titre** : Media Processing API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Pipeline de traitement multimédia. Transcodage vidéo, OCR sur images/PDF, watermarking, compression et détection de contenu. DIFFÉRENCE vs media-api : Media API gère le stockage, CDN et le resize simple d'images, Media Processing API effectue des transformations complexes (transcodage vidéo, OCR, watermark, détection IA de contenu). DIFFÉRENCE vs file-storage-api : File Storage = stockage générique, Media Processing = traitement et transformation du contenu multimédia.

## Endpoints
- **POST** /v1/media-processing/transcode — Transcoder une vidéo (MP4, WebM, HLS, DASH)
  - Requis : source_url, output_format
  - Réponse : 202 — Transcodage lancé — job_id retourné
- **POST** /v1/media-processing/ocr — OCR sur image ou PDF — extraction de texte
  - Requis : source_url
  - Réponse : 200 — Texte extrait avec coordonnées des blocs
- **POST** /v1/media-processing/watermark — Ajouter un watermark (texte ou logo) sur image ou vidéo
  - Requis : source_url, watermark
  - Réponse : 200 — Média avec watermark — URL retournée
- **POST** /v1/media-processing/detect-content — Détection IA de contenu inapproprié (nudité, violence, NSFW)
  - Requis : source_url
  - Réponse : 200 — Résultats de détection avec scores de confiance
- **GET** /v1/media-processing/jobs/{jobId} — Statut d'un job de traitement asynchrone
  - Requis : jobId
  - Réponse : 200 — Statut du job (pending/processing/done/failed)

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# media-storage-api

**Titre** : Media Storage API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Stockage medias. Upload, CDN et transformation images. DIFFERENCE vs document-management-api : Media Storage = fichiers binaires medias CDN, Document Management = GED documents metier.

## Endpoints
- **POST** /v1/media/upload — Uploader media
  - Réponse : 200 — OK
- **GET** /v1/media/{id} — Info media
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/media/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/media/{id}/transform — Transformer image
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/media/{id}/transform — Media transforme
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/media/folders — Dossiers
  - Réponse : 200 — OK
- **POST** /v1/media/folders — Creer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# medical-record-api

**Titre** : Medical Record API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Actes cliniques, diagnostics et historique médical. DIFFÉRENCE vs patient-api : Medical Record = actes médicaux (diagnostics, consultations), Patient API = identité administrative.

## Endpoints
- **GET** /v1/records/{patientId} — Historique actes
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/records/{patientId} — Ajouter acte
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/records/{patientId}/diagnoses — Diagnostics
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/records/{patientId}/diagnoses — Poser diagnostic
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/records/{patientId}/procedures — Actes
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/records/{patientId}/procedures — Enregistrer
  - Requis : patientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# merger-acquisition-api

**Titre** : Merger Acquisition API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Fusions et acquisitions. Data room, closing et integration.

## Endpoints
- **GET** /v1/ma/deals — Operations M&A
  - Réponse : 200 — OK
- **POST** /v1/ma/deals — Ouvrir operation
  - Réponse : 200 — OK
- **GET** /v1/ma/deals/{id} — Detail operation
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/ma/deals/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/ma/deals/{id}/dataroom — Accès data room
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/ma/deals/{id}/dataroom — Uploader document
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/ma/deals/{id}/milestones — Jalons closing
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# mes-api

**Titre** : MES API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Manufacturing Execution System. Supervision atelier, temps reel et KPIs.

## Endpoints
- **GET** /v1/mes/shop-floor — Etat atelier
  - Réponse : 200 — OK
- **GET** /v1/mes/workcenters — Postes de charge
  - Réponse : 200 — OK
- **POST** /v1/mes/workcenters — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/mes/workcenters/{id} — TRS/OEE
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/mes/events — Evenements production
  - Réponse : 200 — OK
- **POST** /v1/mes/events — Enregistrer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# messaging-api

**Titre** : Messaging API
**Version** : v1 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Messagerie bidirectionnelle en temps réel entre utilisateurs. Chat privé, groupes, historique et modération. DIFFÉRENCE CLÉE vs notification-api : Messaging = bidirectionnel (user↔user), Notification = unidirectionnel (système→user). DIFFÉRENCE vs alert-api : Messaging = chat humain, Alert = monitoring système. DIFFÉRENCE vs email-api : Messaging = temps réel in-app, Email = asynchrone externe.

## Endpoints
- **POST** /v1/messages — Envoyer un message (user→user)
  - Réponse : 201 — Envoyé
- **GET** /v1/messages/conversations/{userId} — Lister les conversations d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Conversations
- **GET** /v1/messages/{conversationId} — Historique d'une conversation
  - Requis : conversationId
  - Réponse : 200 — Messages
- **DELETE** /v1/messages/{id} — Supprimer un message (émetteur uniquement)
  - Requis : id
  - Réponse : 204 — Supprimé
- **PUT** /v1/messages/{conversationId}/read — Marquer la conversation comme lue
  - Requis : conversationId
  - Réponse : 200 — Lu

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# metadata-api

**Titre** : Metadata API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Metadonnees techniques fichiers et objets. Schemas, tags et descriptions. DIFFERENCE vs data-catalog-api : Metadata = metadonnees techniques fichiers, Data Catalog = gouvernance enterprise.

## Endpoints
- **GET** /v1/metadata/{resourceId} — Metadonnees
  - Requis : resourceId
  - Réponse : 200 — OK
- **PUT** /v1/metadata/{resourceId} — Mettre a jour
  - Requis : resourceId
  - Réponse : 200 — OK
- **POST** /v1/metadata/{resourceId} — Ajouter tag
  - Requis : resourceId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# metrics-api

**Titre** : Metrics API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Métriques techniques et business. KPIs d'ingénierie (latence, taux d'erreur) et business. DIFFÉRENCE vs analytics-api : Metrics = orienté ingénierie et monitoring, Analytics = orienté business et ventes.

## Endpoints
- **POST** /v1/metrics — Publier une métrique custom
  - Requis : name, value, tags
  - Réponse : 201 — Publiée
- **GET** /v1/metrics/{name} — Récupérer une métrique sur une période
  - Requis : name
  - Réponse : 200 — Métrique
- **GET** /v1/metrics/kpis — KPIs techniques globaux
  - Réponse : 200 — KPIs
- **POST** /v1/metrics/query — Requête avancée multi-métriques
  - Réponse : 200 — Résultats

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# mfa-api

**Titre** : MFA API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Authentification multi-facteurs. TOTP, SMS, et clés hardware (FIDO2/WebAuthn). DIFFÉRENCE vs user-api : MFA API gère tous les facteurs d'authentification (pas seulement le 2FA Google), User API gère l'identité. DIFFÉRENCE vs sms-api : MFA SMS passe par MFA API pour l'OTP d'authentification.

## Endpoints
- **POST** /v1/mfa/enroll — Enrôler un nouveau facteur MFA
  - Requis : user_id, factor_type
  - Réponse : 200 — Facteur enrôlé (secret TOTP ou challenge FIDO2)
- **POST** /v1/mfa/verify — Vérifier un facteur MFA
  - Requis : user_id, factor_type, code
  - Réponse : 200 — Vérifié | 401 — Code invalide
- **GET** /v1/mfa/{userId}/factors — Facteurs MFA actifs d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Facteurs
- **DELETE** /v1/mfa/{userId}/factors/{factorId} — Révoquer un facteur MFA
  - Requis : userId, factorId
  - Réponse : 204 — Révoqué

## Authentification
ApiKeyAuth — apiKey

---

# mini-bar-api

**Titre** : Mini Bar API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Gestion mini-bars hôteliers. Consommations, réapprovisionnement et facturation.

## Endpoints
- **GET** /v1/minibar/{roomId} — Articles mini-bar
  - Requis : roomId
  - Réponse : 200 — OK
- **POST** /v1/minibar/{roomId} — Enregistrer consommation
  - Requis : roomId
  - Réponse : 200 — OK
- **PUT** /v1/minibar/{roomId} — Réapprovisionner
  - Requis : roomId
  - Réponse : 200 — OK
- **GET** /v1/minibar/{bookingId}/bill — Facture consommations
  - Requis : bookingId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# model-registry-api

**Titre** : Model Registry API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Registre modeles ML. Versions, metriques et deploiement.

## Endpoints
- **GET** /v1/models — Modeles
  - Réponse : 200 — OK
- **POST** /v1/models — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/models/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/models/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/models/{id}/versions — Versions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/models/{id}/versions — Ajouter
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/models/{id}/versions/{version}/deploy — Deployer
  - Requis : id, version
  - Réponse : 200 — OK
- **DELETE** /v1/models/{id}/versions/{version}/deploy — Retirer
  - Requis : id, version
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# mortgage-api-v1

**Titre** : Mortgage API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Prets immobiliers v1. DEPRECATED.

## Endpoints
- **GET** /v1/mortgages — Lister
  - Réponse : 200 — OK
- **POST** /v1/mortgages — Demander
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# mortgage-api-v2

**Titre** : Mortgage API
**Version** : v2 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Prets immobiliers avec hypotheque. Tableau d'amortissement et mainlevee. DIFFERENCE vs loan-api : Mortgage = credit immobilier avec garantie, Loan = pret sans garantie.

## Endpoints
- **GET** /v2/mortgages — Portefeuille
  - Réponse : 200 — OK
- **POST** /v2/mortgages — Demander
  - Réponse : 200 — OK
- **GET** /v2/mortgages/{id} — Dossier complet
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/mortgages/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/mortgages/{id}/amortization — Tableau amortissement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/mortgages/{id}/discharge — Mainlevee hypotheque
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# mrp-api

**Titre** : MRP API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Material Requirements Planning. Calcul besoins, suggestions et lancement. DIFFERENCE vs inventory-api : MRP = calcul besoins futurs selon planification, Inventory = stock physique actuel.

## Endpoints
- **POST** /v1/mrp/calculate — Calculer besoins MRP
  - Réponse : 200 — OK
- **GET** /v1/mrp/suggestions — Suggestions approvisionnement
  - Réponse : 200 — OK
- **POST** /v1/mrp/suggestions — Accepter suggestion
  - Réponse : 200 — OK
- **GET** /v1/mrp/plan/{productId} — Plan de production
  - Requis : productId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# mvno-api

**Titre** : MVNO API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Operateurs virtuels MVNO. Accords, decomptes et marges.

## Endpoints
- **GET** /v1/mvno/partners — MVNO
  - Réponse : 200 — OK
- **POST** /v1/mvno/partners — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/mvno/partners/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/mvno/partners/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/mvno/partners/{id}/settlement — Decompte
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/mvno/partners/{id}/settlement — Generer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# network-api

**Titre** : Network API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Gestion reseau telecom. Noeuds, couverture et qualite de service.

## Endpoints
- **GET** /v1/network/nodes — Noeuds
  - Réponse : 200 — OK
- **POST** /v1/network/nodes — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/network/coverage/{location} — Couverture
  - Requis : location
  - Réponse : 200 — OK
- **GET** /v1/network/qos — Metriques QoS
  - Réponse : 200 — OK
- **GET** /v1/network/incidents — Incidents
  - Réponse : 200 — OK
- **POST** /v1/network/incidents — Signaler
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# network-quality-api

**Titre** : Network Quality API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Qualite reseau et SLA. DIFFERENCE vs network-api : Network Quality = metriques QoS/SLA, Network = infrastructure noeuds.

## Endpoints
- **GET** /v1/network-quality/{siteId} — Qualite
  - Requis : siteId
  - Réponse : 200 — OK
- **POST** /v1/network-quality/{siteId} — Tester
  - Requis : siteId
  - Réponse : 200 — OK
- **GET** /v1/network-quality/sla — Violations
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# network-segmentation-api

**Titre** : Network Segmentation API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Segmentation reseau. VLANs, micro-segmentation et firewall rules.

## Endpoints
- **GET** /v1/segmentation/zones — Zones reseau
  - Réponse : 200 — OK
- **POST** /v1/segmentation/zones — Creer zone
  - Réponse : 200 — OK
- **GET** /v1/segmentation/rules — Regles
  - Réponse : 200 — OK
- **POST** /v1/segmentation/rules — Ajouter regle
  - Réponse : 200 — OK
- **DELETE** /v1/segmentation/rules — Supprimer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# notary-api

**Titre** : Notary API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Actes notaries. Ventes immobilières, successions et authentification.

## Endpoints
- **GET** /v1/notary/acts — Actes en cours
  - Réponse : 200 — OK
- **POST** /v1/notary/acts — Créer acte
  - Réponse : 200 — OK
- **GET** /v1/notary/acts/{id} — Detail acte
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/notary/acts/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/notary/acts/{id} — Authentifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/notary/acts/{id}/parties — Parties
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/notary/acts/{id}/parties — Ajouter partie
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/notary/acts/{id}/archive — Archiver au rang des minutes
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# notification-api-v1

**Titre** : Notification API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Notifications v1. DEPRECATED.

## Endpoints
- **POST** /v1/notifications — Envoyer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# notification-api-v2

**Titre** : Notification API
**Version** : v2 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Version 2 de la Notification API. Ajout des templates multilingues, des préférences utilisateur par canal et du retry automatique. DIFFÉRENCE vs v1 : templates versionnés, opt-out par canal, batching asynchrone.

## Endpoints
- **POST** /v2/notifications/send — Envoyer via template ou message brut, multi-canal
  - Réponse : 201 — Envoyée | 400 — 
- **POST** /v2/notifications/batch — Envoi groupé asynchrone (max 50 000 destinataires)
  - Réponse : 202 — Job asynchrone créé
- **GET** /v2/notifications/{id} — Statut et logs de livraison
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **DELETE** /v2/notifications/{id} — Annuler si pending
  - Requis : id
  - Réponse : 204 — Annulée | 409 — 
- **GET** /v2/notifications/preferences/{userId} — Préférences de notification d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Préférences
- **PUT** /v2/notifications/preferences/{userId} — Mettre à jour les préférences (opt-out par canal)
  - Requis : userId
  - Réponse : 200 — Mis à jour
- **GET** /v2/notifications/templates — Lister les templates de notification
  - Réponse : 200 — Templates
- **POST** /v2/notifications/templates — Créer un template multilingue
  - Requis : name, content
  - Réponse : 201 — Template créé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# notification-api-v3

**Titre** : Notification API
**Version** : v3 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Version actuelle. Ajout des canaux WhatsApp et in-app, du système de règles de déclenchement (triggers), de la personnalisation IA et du rate-limiting par utilisateur. DIFFÉRENCE vs notification-api-v2 : v3 ajoute WhatsApp, les triggers événementiels et la personnalisation IA des contenus.

## Endpoints
- **POST** /v3/notifications/send — Envoyer (email/SMS/push/WhatsApp/in-app) avec personnalisation IA
  - Réponse : 201 — Envoyée | 429 — Rate limit utilisateur atteint
- **POST** /v3/notifications/triggers — Créer une règle de déclenchement événementielle (nouveau en v3)
  - Requis : name, event, template_id
  - Réponse : 201 — Trigger créé
- **GET** /v3/notifications/triggers — Lister les règles de déclenchement
  - Réponse : 200 — Triggers
- **GET** /v3/notifications/in-app/{userId} — Notifications in-app non lues d'un utilisateur (nouveau canal v3)
  - Requis : userId
  - Réponse : 200 — Notifications
- **PATCH** /v3/notifications/in-app/{userId} — Marquer en lues
  - Requis : userId
  - Réponse : 200 — Mises à jour
- **GET** /v3/notifications/{id} — Statut et logs de livraison
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/notifications/{id} — Annuler si pending
  - Requis : id
  - Réponse : 204 — Annulée | 409 — 

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# notification-api

**Titre** : Notification API
**Version** : v1 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Orchestrateur de notifications multicanal (email, SMS, push) vers les utilisateurs finaux. DIFFÉRENCE vs email-api : Notification = façade multi-canal, Email = canal email seul avec templates. DIFFÉRENCE vs messaging-api : Notification = unidirectionnel (système→user), Messaging = bidirectionnel (user↔user). DIFFÉRENCE vs alert-api : Notification cible les clients, Alert cible les équipes ops. DIFFÉRENCE vs sms-api : Notification orchestre tous les canaux, SMS = canal SMS seul.

## Endpoints
- **POST** /v1/notifications/send — Envoyer une notification immédiate multicanal
  - Réponse : 201 — Envoyée | 400 — 
- **POST** /v1/notifications/schedule — Planifier une notification future
  - Réponse : 201 — Planifiée
- **GET** /v1/notifications/{id} — Statut d'une notification
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **DELETE** /v1/notifications/{id} — Annuler (statut pending uniquement)
  - Requis : id
  - Réponse : 204 — Annulée | 409 — 
- **GET** /v1/notifications — Lister avec filtres
  - Réponse : 200 — Liste
- **GET** /v1/notifications/stats — Statistiques d'envoi par canal
  - Réponse : 200 — Stats

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# number-lookup-api

**Titre** : Number Lookup API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Identification numeros telephone. DIFFERENCE vs iban-validation-api : Number Lookup = numero telephone, IBAN Validation = IBAN bancaire.

## Endpoints
- **GET** /v1/lookup/{number} — Operateur
  - Requis : number
  - Réponse : 200 — OK
- **POST** /v1/lookup/batch — Identification masse
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# number-management-api

**Titre** : Number Management API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Gestion numeros. Attribution, portabilite et SDA.

## Endpoints
- **GET** /v1/numbers — Numeros
  - Réponse : 200 — OK
- **POST** /v1/numbers — Attribuer
  - Réponse : 200 — OK
- **GET** /v1/numbers/{number} — Info
  - Requis : number
  - Réponse : 200 — OK
- **DELETE** /v1/numbers/{number} — Liberer
  - Requis : number
  - Réponse : 200 — OK
- **POST** /v1/numbers/{number}/portability — Initier portabilite
  - Requis : number
  - Réponse : 200 — OK
- **GET** /v1/numbers/{number}/portability — Statut
  - Requis : number
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# number-portability-api

**Titre** : Number Portability API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Portabilite numeros entre operateurs. Demandes, statuts et delais.

## Endpoints
- **GET** /v1/portability/requests — Demandes
  - Réponse : 200 — OK
- **POST** /v1/portability/requests — Soumettre
  - Réponse : 200 — OK
- **GET** /v1/portability/requests/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/portability/requests/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# occupancy-api

**Titre** : Occupancy API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Taux d'occupation et disponibilités. Baux actifs, vacances et prévisions.

## Endpoints
- **GET** /v1/occupancy/{portfolioId} — Vacances
  - Requis : portfolioId
  - Réponse : 200 — OK
- **GET** /v1/occupancy/{portfolioId}/forecast — Prévisions
  - Requis : portfolioId
  - Réponse : 200 — OK
- **GET** /v1/occupancy/alerts — Alertes vacance
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# oee-api

**Titre** : OEE API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Calcul TRS/OEE. Disponibilite, performance et qualite machines.

## Endpoints
- **GET** /v1/oee/{machineId} — Decomposition TRS
  - Requis : machineId
  - Réponse : 200 — OK
- **GET** /v1/oee/{machineId}/history — Historique TRS
  - Requis : machineId
  - Réponse : 200 — OK
- **GET** /v1/oee/site — TRS par equipe
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# onboarding-api

**Titre** : Onboarding API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Parcours d'intégration des nouveaux employés. Checklist, documents et accès à provisionner.

## Endpoints
- **POST** /v1/onboarding/start — Démarrer le parcours d'onboarding
  - Requis : employee_id, start_date
  - Réponse : 201 — Parcours démarré
- **GET** /v1/onboarding/{employeeId} — Statut du parcours d'onboarding
  - Requis : employeeId
  - Réponse : 200 — Parcours avec tâches et avancement
- **PUT** /v1/onboarding/{employeeId}/tasks/{taskId}/complete — Marquer une tâche d'onboarding comme complétée
  - Requis : employeeId, taskId
  - Réponse : 200 — Tâche complétée
- **POST** /v1/onboarding/{employeeId}/provision-access — Provisionner automatiquement les accès systèmes
  - Requis : employeeId
  - Réponse : 202 — Accès provisionnés

## Authentification
ApiKeyAuth — apiKey

---

# open-banking-api

**Titre** : Open Banking API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Open banking PSD2. Agregation comptes multi-banques et initiation paiement.

## Endpoints
- **GET** /v1/ob/accounts — Comptes agreges
  - Réponse : 200 — OK
- **POST** /v1/ob/consent — Creer consentement TPP
  - Réponse : 200 — OK
- **DELETE** /v1/ob/consent — Revoquer
  - Réponse : 200 — OK
- **POST** /v1/ob/payments — Initier paiement PSD2
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# order-api

**Titre** : Order API
**Version** : v1 | **Statut** : deprecated
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Version initiale de l'API commandes. DEPRECATED depuis 2021. Ne supporte qu'un seul produit par commande, IDs entiers, pas de remises ni de pagination. Migrer vers v2.

## Endpoints
- POST /v1/orders — Créer une commande (mono-produit)
- GET /v1/orders — Lister les commandes
- GET /v1/orders/{id} — Récupérer une commande
- DELETE /v1/orders/{id} — Supprimer une commande — BREAKING: remplacé par /cancel en v2

---

# order-api

**Titre** : Order API
**Version** : v2 | **Statut** : deprecated
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Version 2 — DEPRECATED juin 2022. Introduit multi-articles, IDs préfixés ORD-, pagination et codes promo. Incompatible v1.

## Endpoints
- POST /v2/orders — Créer une commande multi-articles
- GET /v2/orders — Lister avec pagination
- GET /v2/orders/{id} — Récupérer une commande
- PUT /v2/orders/{id} — Modifier le statut
- PUT /v2/orders/{id}/cancel — Annuler une commande

---

# order-api

**Titre** : Order API
**Version** : v3 | **Statut** : deprecated
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Version 3 — DEPRECATED sept. 2023. Adresse structurée, statut partially_shipped, objet discount enrichi.

## Endpoints
- POST /v3/orders — Créer une commande avec adresse structurée
- GET /v3/orders — Lister avec filtres avancés
- GET /v3/orders/{id} — Récupérer une commande
- PUT /v3/orders/{id} — Modifier (avant expédition)
- PUT /v3/orders/{id}/cancel — Annuler avec option remboursement

---

# order-api

**Titre** : Order API
**Version** : v4 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Version actuelle et recommandée. Gestion complète du cycle de vie des commandes e-commerce. Multi-articles, multi-devises, webhooks automatiques, expédition partielle. Utiliser cette version pour tous les nouveaux développements.

## Endpoints
- POST /v4/orders — Créer une commande complète
- GET /v4/orders — Lister avec filtres complets et tri
- GET /v4/orders/{id} — Récupérer une commande avec détails complets
- PUT /v4/orders/{id} — Modifier une commande (avant confirmation uniquement)
- DELETE /v4/orders/{id} — Supprimer (statut cancelled uniquement)

---

# order-management-api-v1

**Titre** : Order Management API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Commandes v1. DEPRECATED.

## Endpoints
- **GET** /v1/orders — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# order-management-api-v2

**Titre** : Order Management API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Commandes v2 avec suivi. DEPRECATED.

## Endpoints
- **GET** /v2/orders — Lister
  - Réponse : 200 — OK
- **POST** /v2/orders — Créer
  - Réponse : 200 — OK
- **GET** /v2/orders/{id}/track — Suivre
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# order-management-api-v3

**Titre** : Order Management API
**Version** : v3 | **Statut** : active
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Gestion commandes omnicanal. Cycle de vie, fractionnement et retours. DIFFERENCE vs cart-api : Order Management = commande validée et en cours de traitement, Cart = panier en cours de constitution.

## Endpoints
- **GET** /v3/orders — Commandes
  - Réponse : 200 — OK
- **POST** /v3/orders — Créer commande
  - Réponse : 200 — OK
- **GET** /v3/orders/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/orders/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/orders/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/orders/{id}/status — Statut
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/orders/{id}/status — Changer statut
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/orders/{id}/returns — Retours
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/orders/{id}/returns — Initier retour
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# org-api

**Titre** : Organization API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Structure organisationnelle. Entités légales, filiales et hiérarchie de l'entreprise. DIFFÉRENCE vs hr-api : Org API gère la structure juridique et les entités légales, HR API gère les employés et leurs dossiers.

## Endpoints
- **GET** /v1/organizations — Lister les entités organisationnelles
  - Réponse : 200 — Entités
- **POST** /v1/organizations — Créer une entité légale
  - Requis : name, type
  - Réponse : 201 — Créée
- **GET** /v1/organizations/{id} — Détails d'une entité
  - Requis : id
  - Réponse : 200 — Entité | 404 — 
- **GET** /v1/organizations/{id}/headcount — Effectif d'une entité
  - Requis : id
  - Réponse : 200 — Effectif par département

## Authentification
ApiKeyAuth — apiKey

---

# packaging-api

**Titre** : Packaging API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Gestion emballages. References, conditionnements et gestion retours.

## Endpoints
- **GET** /v1/packaging — Types emballage
  - Réponse : 200 — OK
- **POST** /v1/packaging — Ajouter
  - Réponse : 200 — OK
- **POST** /v1/packaging/{orderId}/pack — Conditionner ordre
  - Requis : orderId
  - Réponse : 200 — OK
- **GET** /v1/packaging/{orderId}/pack — Liste colisage
  - Requis : orderId
  - Réponse : 200 — OK
- **GET** /v1/packaging/returns — Retours emballages
  - Réponse : 200 — OK
- **POST** /v1/packaging/returns — Traiter retour
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# parent-portal-api

**Titre** : Parent Portal API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Espace parents. Suivi scolaire, communications et paiements.

## Endpoints
- **GET** /v1/parent/{parentId} — Informations parent
  - Requis : parentId
  - Réponse : 200 — OK
- **GET** /v1/parent/{parentId}/children — Progression enfants
  - Requis : parentId
  - Réponse : 200 — OK
- **GET** /v1/parent/{parentId}/messages — Messages
  - Requis : parentId
  - Réponse : 200 — OK
- **POST** /v1/parent/{parentId}/messages — Envoyer message
  - Requis : parentId
  - Réponse : 200 — OK
- **GET** /v1/parent/{parentId}/payments — Paiements scolarité
  - Requis : parentId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# parking-api-v1

**Titre** : Parking API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Stationnement v1. DEPRECATED.

## Endpoints
- **GET** /v1/parking — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# parking-api-v2

**Titre** : Parking API
**Version** : v2 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion parkings et stationnement. Disponibilité, réservation et paiement. DIFFERENCE vs ev-charging-api : Parking = stationnement generique, EV Charging = recharge véhicules électriques spécifiquement.

## Endpoints
- **GET** /v2/parking — Parkings disponibles
  - Réponse : 200 — OK
- **POST** /v2/parking — Réserver place
  - Réponse : 200 — OK
- **GET** /v2/parking/{id} — Disponibilité
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/parking/{id}/payment — Payer stationnement
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# patient-admission-api

**Titre** : Patient Admission API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Admission et sortie administrative. Check-in, attribution lit et facturation séjour. DIFFÉRENCE vs emergency-api : Admission = entrée planifiée, Emergency = urgences non planifiées.

## Endpoints
- **GET** /v1/admissions — Admissions en cours
  - Réponse : 200 — OK
- **POST** /v1/admissions — Admettre
  - Réponse : 200 — OK
- **GET** /v1/admissions/{id} — Dossier
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/admissions/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/admissions/{id}/discharge — Sortie administrative
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# patient-api-v1

**Titre** : Patient API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Gestion basique des dossiers patients. DEPRECATED — migrer vers v3.

## Endpoints
- **GET** /v1/patients — Lister patients
  - Réponse : 200 — OK
- **POST** /v1/patients — Créer patient
  - Réponse : 200 — OK
- **GET** /v1/patients/{id} — Détail patient
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/patients/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# patient-api-v2

**Titre** : Patient API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Version 2 avec dossier médical structuré. DEPRECATED.

## Endpoints
- **GET** /v2/patients — Lister
  - Réponse : 200 — OK
- **POST** /v2/patients — Créer
  - Réponse : 200 — OK
- **GET** /v2/patients/{id}/consultations — Historique
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/patients/{id}/consultations — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# patient-api-v3

**Titre** : Patient API
**Version** : v3 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Dossier patient complet HL7 FHIR avec consentements RGPD et alertes médicales. DIFFÉRENCE vs medical-record-api : Patient API = identité et admission, Medical Record = actes cliniques.

## Endpoints
- **GET** /v3/patients — Lister avec filtres FHIR
  - Réponse : 200 — OK
- **POST** /v3/patients — Admettre patient
  - Réponse : 200 — OK
- **GET** /v3/patients/{id} — Dossier FHIR complet
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/patients/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/patients/{id} — Sortie patient
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/patients/{id}/alerts — Alertes médicales
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/patients/{id}/alerts — Créer alerte
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/patients/{id}/consent — Consentements RGPD
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/patients/{id}/consent — Modifier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# payment-api-v1

**Titre** : Payment API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version 1 de l'API paiement. DEPRECATED 2022. Supporte uniquement les paiements carte, pas de PayPal ni SEPA. Remboursements manuels uniquement. Migrer vers v2.

## Endpoints
- **POST** /v1/payments — Créer un paiement carte (seul canal supporté)
  - Réponse : 201 — Paiement initié | 402 — Refusé
- **GET** /v1/payments/{id} — Statut du paiement
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **DELETE** /v1/payments/{id} — Annuler (BREAKING v2: remplacé par /refund)
  - Requis : id
  - Réponse : 200 — Annulé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# payment-api-v2

**Titre** : Payment API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version 2 de l'API paiement — DEPRECATED depuis 2024, migrer vers v3. Introduit PayPal et SEPA, le mode capture manuelle et les remboursements partiels. Incompatible avec v1 (ID integer → string PAY-XXXX).

## Endpoints
- **POST** /v2/payments — Initier paiement (card/PayPal/SEPA)
  - Réponse : 201 — Initié | 402 — Refusé
- **GET** /v2/payments — Lister les paiements
  - Réponse : 200 — Paiements
- **GET** /v2/payments/{id} — Statut d'un paiement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/payments/{id}/capture — Capturer un paiement pré-autorisé (mode manual)
  - Requis : id
  - Réponse : 200 — Capturé
- **POST** /v2/payments/{id}/refund — Remboursement total ou partiel
  - Requis : id
  - Réponse : 200 — Remboursement initié

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# payment-api-v3

**Titre** : Payment API
**Version** : v3 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Version 3 Payment. Paiements crypto, paiement en plusieurs fois (BNPL) et réconciliation bancaire automatique. DIFFÉRENCE vs v2 : ajout BNPL (Klarna/Alma), crypto (BTC/ETH), réconciliation.

## Endpoints
- **POST** /v3/payments — Initier un paiement (card/paypal/sepa/bnpl/crypto)
  - Requis : amount, currency, method, order_id
  - Réponse : 201 — Initié | 402 — Refusé
- **POST** /v3/payments/{id}/dispute — Contester un paiement (chargeback)
  - Requis : id, reason
  - Réponse : 201 — Dispute ouverte
- **POST** /v3/payments/reconciliation — Lancer la réconciliation bancaire
  - Requis : period
  - Réponse : 202 — Réconciliation lancée

## Authentification
ApiKeyAuth — apiKey

---

# payment-api

**Titre** : Payment API
**Version** : v2 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Traitement des transactions de paiement ponctuelles. Carte bancaire, PayPal, virement SEPA, remboursements. DIFFÉRENCE vs billing-api : Payment traite UNE transaction, Billing gère les cycles récurrents. DIFFÉRENCE vs invoice-api : Payment effectue le paiement, Invoice génère le document fiscal. DIFFÉRENCE vs wallet-api : Payment traite les paiements externes (carte/bank), Wallet gère le solde interne.

## Endpoints
- **POST** /v2/payments — Initier un paiement
  - Réponse : 201 — Initié | 400 —  | 402 — Paiement refusé par l'émetteur
- **GET** /v2/payments/{id} — Statut d'un paiement
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **POST** /v2/payments/{id}/refund — Rembourser (total ou partiel)
  - Requis : id
  - Réponse : 200 — Remboursement initié
- **POST** /v2/payments/capture — Capturer un paiement pré-autorisé
  - Requis : authorization_id
  - Réponse : 200 — Capturé
- **GET** /v2/payments?orderId={id} — Paiements d'une commande
  - Requis : orderId
  - Réponse : 200 — Paiements

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# payout-api

**Titre** : Payout API
**Version** : v1 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Versements aux vendeurs et partenaires. Marketplace payouts, virements SEPA et suivi. DIFFÉRENCE vs payment-api : Payout = versement DE nous VERS un tiers (vendeur, partenaire), Payment = encaissement D'un client VERS nous.

## Endpoints
- **POST** /v1/payouts — Créer un virement vers un bénéficiaire
  - Requis : recipient_id, amount, currency
  - Réponse : 201 — Virement créé
- **GET** /v1/payouts — Lister les virements
  - Réponse : 200 — Virements
- **GET** /v1/payouts/{id} — Statut d'un virement
  - Requis : id
  - Réponse : 200 — Virement | 404 — 
- **POST** /v1/payouts/batch — Virement en masse (max 1000)
  - Requis : payouts
  - Réponse : 202 — Virements groupés traités

## Authentification
ApiKeyAuth — apiKey

---

# payroll-api

**Titre** : Payroll API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Paie et bulletins de salaire. Calcul des rémunérations, charges sociales et virements. DIFFÉRENCE vs billing-api : Payroll concerne les salaires des employés, Billing concerne la facturation clients.

## Endpoints
- **POST** /v1/payroll/run — Lancer le calcul de la paie du mois
  - Requis : month, year
  - Réponse : 202 — Calcul lancé
- **GET** /v1/payroll/{employeeId}/slips — Liste des bulletins de salaire
  - Requis : employeeId
  - Réponse : 200 — Bulletins
- **GET** /v1/payroll/{employeeId}/slips/{month} — Bulletin d'un mois spécifique
  - Requis : employeeId, month
  - Réponse : 200 — Bulletin
- **POST** /v1/payroll/simulate — Simuler la paie d'un employé
  - Réponse : 200 — Simulation

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# penetration-test-api

**Titre** : Penetration Test API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Tests d'intrusion. Planification, exécution et rapports.

## Endpoints
- **GET** /v1/pentests — Tests planifiés
  - Réponse : 200 — OK
- **POST** /v1/pentests — Créer test
  - Réponse : 200 — OK
- **GET** /v1/pentests/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/pentests/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/pentests/{id} — Lancer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/pentests/{id}/findings — Résultats
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/pentests/{id}/findings — Ajouter finding
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/pentests/{id}/report — Rapport final
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# performance-api

**Titre** : Performance API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Évaluations de performance. OKRs, feedback 360° et plans de développement.

## Endpoints
- **POST** /v1/performance/reviews — Créer une évaluation de performance
  - Requis : employee_id, period, reviewer_id
  - Réponse : 201 — Créée
- **GET** /v1/performance/{employeeId} — Historique des évaluations
  - Requis : employeeId
  - Réponse : 200 — Évaluations
- **POST** /v1/performance/objectives — Créer un objectif (OKR)
  - Requis : employee_id, title, period
  - Réponse : 201 — Objectif créé
- **PUT** /v1/performance/objectives/{id}/progress — Mettre à jour la progression d'un objectif
  - Requis : id, progress
  - Réponse : 200 — Progression mise à jour

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# permission-api

**Titre** : Permission API
**Version** : v1 | **Statut** : active
**Domaine** : Security & Compliance | **Équipe** : Equipe Security

## Description
Contrôle d'accès basé sur les rôles (RBAC). Permissions, rôles et politique d'accès. DIFFÉRENCE vs auth-api : Auth = authentification (qui es-tu ?), Permission = autorisation (qu'as-tu le droit de faire ?).

## Endpoints
- **GET** /v1/permissions — Lister toutes les permissions
  - Réponse : 200 — Permissions
- **POST** /v1/permissions — Créer une permission
  - Requis : name, resource, action
  - Réponse : 201 — Créée
- **GET** /v1/roles — Lister les rôles
  - Réponse : 200 — Rôles
- **POST** /v1/roles — Créer un rôle
  - Requis : name
  - Réponse : 201 — Créé
- **GET** /v1/users/{userId}/roles — Rôles d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Rôles
- **POST** /v1/users/{userId}/roles — Assigner un rôle
  - Requis : userId, role_id
  - Réponse : 200 — Assigné
- **DELETE** /v1/users/{userId}/roles — Révoquer un rôle
  - Requis : userId, role_id
  - Réponse : 200 — Révoqué
- **POST** /v1/check — Vérifier si un utilisateur a une permission
  - Requis : user_id, resource, action
  - Réponse : 200 — allowed: true/false

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# pest-detection-api

**Titre** : Pest Detection API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Détection ravageurs et maladies. Identification IA par photo et traitements recommandés.

## Endpoints
- **POST** /v1/pests/detect — Identifier ravageur/maladie par photo
  - Réponse : 200 — OK
- **GET** /v1/pests/{fieldId}/monitoring — Surveillance active
  - Requis : fieldId
  - Réponse : 200 — OK
- **POST** /v1/pests/{fieldId}/monitoring — Signaler observation
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v1/pests/treatments — Traitements disponibles
  - Réponse : 200 — OK
- **POST** /v1/pests/treatments — Recommander traitement
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# pharmacy-api

**Titre** : Pharmacy API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Stock pharmaceutique, dispensation et traçabilité médicaments. Alertes péremption et ruptures.

## Endpoints
- **GET** /v1/drugs — Stock médicaments
  - Réponse : 200 — OK
- **POST** /v1/drugs — Référencer
  - Réponse : 200 — OK
- **GET** /v1/drugs/{id} — Fiche médicament
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/drugs/{id} — Mise à jour stock
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/dispensations — Historique
  - Réponse : 200 — OK
- **POST** /v1/dispensations — Dispenser
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# pipeline-api

**Titre** : Pipeline API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Pipelines de donnees. Orchestration, monitoring et alertes.

## Endpoints
- **GET** /v1/pipelines — Pipelines
  - Réponse : 200 — OK
- **POST** /v1/pipelines — Creer
  - Réponse : 200 — OK
- **GET** /v1/pipelines/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/pipelines/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/pipelines/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/pipelines/{id}/runs — Executions
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/pipelines/{id}/runs — Declencher
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/pipelines/{id}/runs/{runId} — Statut
  - Requis : id, runId
  - Réponse : 200 — OK
- **DELETE** /v1/pipelines/{id}/runs/{runId} — Annuler
  - Requis : id, runId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# plagiarism-detection-api

**Titre** : Plagiarism Detection API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Détection de plagiat. Analyse similarité et rapport détaillé.

## Endpoints
- **POST** /v1/plagiarism/check — Analyser document
  - Réponse : 200 — OK
- **GET** /v1/plagiarism/reports/{documentId} — Documents similaires
  - Requis : documentId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# plan-api-v1

**Titre** : Plan API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Forfaits v1. DEPRECATED.

## Endpoints
- **GET** /v1/plans — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# plan-api-v2

**Titre** : Plan API
**Version** : v2 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Forfaits voix, data et mixtes. DIFFERENCE vs subscription-api : Plan = forfait telecom quota data/voix, Subscription = abonnement logiciel.

## Endpoints
- **GET** /v2/plans — Catalogue
  - Réponse : 200 — OK
- **POST** /v2/plans — Creer
  - Réponse : 200 — OK
- **GET** /v2/plans/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/plans/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/plans/{id}/subscribe — Souscrire
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/plans/{id}/migrate — Migrer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# policy-api-v1

**Titre** : Policy API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Contrats assurance v1. DEPRECATED.

## Endpoints
- **GET** /v1/policies — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# policy-api-v2

**Titre** : Policy API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Contrats assurance v2. DEPRECATED.

## Endpoints
- **GET** /v2/policies — Lister
  - Réponse : 200 — OK
- **POST** /v2/policies — Souscrire
  - Réponse : 200 — OK
- **POST** /v2/policies/{id}/endorsements — Avenant
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# policy-api-v3

**Titre** : Policy API
**Version** : v3 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Contrats d'assurance complets. Souscription, avenants, renouvellement et résiliation.

## Endpoints
- **GET** /v3/policies — Portefeuille contrats
  - Réponse : 200 — OK
- **POST** /v3/policies — Souscrire contrat
  - Réponse : 200 — OK
- **GET** /v3/policies/{id} — Detail contrat
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/policies/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/policies/{id}/endorsements — Avenants
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/policies/{id}/endorsements — Créer avenant
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/policies/{id}/renewal — Info renouvellement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/policies/{id}/renewal — Renouveler
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/policies/{id}/cancel — Résilier contrat
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# portfolio-api

**Titre** : Portfolio API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Gestion portefeuille actifs. Valorisation, performance et rebalancement. DIFFERENCE vs investment-api : Portfolio = analyse existant, Investment = passation ordres.

## Endpoints
- **GET** /v1/portfolios/{clientId} — Valorisation
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v1/portfolios/{clientId} — Creer
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/portfolios/{id}/performance — Performance TRI
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/portfolios/{id}/rebalance — Reequilibrer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# pos-api

**Titre** : POS API
**Version** : v1 | **Statut** : active
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Point of Sale en magasin. Transactions, tiroir-caisse et reçus.

## Endpoints
- **GET** /v1/pos/transactions — Transactions
  - Réponse : 200 — OK
- **POST** /v1/pos/transactions — Créer vente
  - Réponse : 200 — OK
- **GET** /v1/pos/transactions/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/pos/transactions/{id} — Annuler vente
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/pos/sessions — Session ouverte
  - Réponse : 200 — OK
- **POST** /v1/pos/sessions — Fermer caisse
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# power-of-attorney-api

**Titre** : Power of Attorney API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Procurations et mandats. Creation, validation et revocation.

## Endpoints
- **GET** /v1/poa — Procurations actives
  - Réponse : 200 — OK
- **POST** /v1/poa — Créer procuration
  - Réponse : 200 — OK
- **GET** /v1/poa/{id} — Detail procuration
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/poa/{id} — Valider
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/poa/{id} — Révoquer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/poa/{id}/scope — Périmètre delegation
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/poa/{id}/scope — Modifier périmètre
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# pre-order-api

**Titre** : Pre-Order API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Pré-commandes pour produits non encore disponibles. Réservation, paiement différé et notifications de disponibilité.

## Endpoints
- **POST** /v1/pre-orders — Créer une pré-commande
  - Requis : customer_id, product_id
  - Réponse : 201 — Pré-commande créée
- **GET** /v1/pre-orders/{id} — Statut d'une pré-commande
  - Requis : id
  - Réponse : 200 — Pré-commande | 404 — 
- **DELETE** /v1/pre-orders/{id} — Annuler une pré-commande
  - Requis : id
  - Réponse : 200 — Annulée
- **POST** /v1/pre-orders/product/{productId}/availability — Notifier les clients en pré-commande que le produit est disponible
  - Requis : productId
  - Réponse : 202 — Notifications envoyées — paiements déclenchés

## Authentification
ApiKeyAuth — apiKey

---

# precision-farming-api

**Titre** : Precision Farming API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Agriculture de precision. Modulation intra-parcellaire, cartes de rendement et prescriptions variables.

## Endpoints
- **GET** /v1/precision/{fieldId} — Carte prescription
  - Requis : fieldId
  - Réponse : 200 — OK
- **POST** /v1/precision/{fieldId} — Creer prescription
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v1/precision/{fieldId}/yield-map — Carte rendement
  - Requis : fieldId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# predictive-maintenance-api

**Titre** : Predictive Maintenance API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Maintenance prédictive ML sur équipements industriels. Détection pannes anticipées et recommandations.

## Endpoints
- **GET** /v1/maintenance/predictions/{deviceId} — Prédictions pannes
  - Requis : deviceId
  - Réponse : 200 — OK
- **POST** /v1/maintenance/predictions/{deviceId} — Lancer analyse
  - Requis : deviceId
  - Réponse : 200 — OK
- **GET** /v1/maintenance/alerts — Alertes maintenance
  - Réponse : 200 — OK
- **PUT** /v1/maintenance/alerts — Acquitter
  - Réponse : 200 — OK
- **GET** /v1/maintenance/history/{deviceId} — Historique interventions
  - Requis : deviceId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# premium-calculation-api

**Titre** : Premium Calculation API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Calcul primes d'assurance. Tarification actuarielle et comparaison.

## Endpoints
- **POST** /v1/premium/calculate — Calculer prime
  - Réponse : 200 — OK
- **POST** /v1/premium/compare — Comparer offres
  - Réponse : 200 — OK
- **GET** /v1/premium/{policyId} — Prime actuelle
  - Requis : policyId
  - Réponse : 200 — OK
- **GET** /v1/premium/history/{clientId} — Historique primes
  - Requis : clientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# prescription-api-v1

**Titre** : Prescription API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Ordonnances médicales version 1. DEPRECATED.

## Endpoints
- **GET** /v1/prescriptions — Lister
  - Réponse : 200 — OK
- **POST** /v1/prescriptions — Créer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# prescription-api-v2

**Titre** : Prescription API
**Version** : v2 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Ordonnances électroniques sécurisées avec signature numérique et envoi pharmacie. DIFFÉRENCE vs drug-interaction-api : Prescription = document légal, Drug Interaction = vérification incompatibilités.

## Endpoints
- **GET** /v2/prescriptions — Lister
  - Réponse : 200 — OK
- **POST** /v2/prescriptions — Créer ordonnance
  - Réponse : 200 — OK
- **GET** /v2/prescriptions/{id} — Détail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/prescriptions/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/prescriptions/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/prescriptions/{id}/dispense — Marquer dispensée
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/prescriptions/{id}/renew — Renouveler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# price-list-api

**Titre** : Price List API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Listes de prix et catalogues tarifaires B2B. Prix négociés par client ou groupe. DIFFÉRENCE vs pricing-api : Price List = prix contractuels statiques par client/groupe (B2B), Pricing API = calcul dynamique temps réel avec règles promotionnelles.

## Endpoints
- **POST** /v1/price-lists — Créer une liste de prix
  - Réponse : 201 — Créée
- **GET** /v1/price-lists — Lister les listes de prix
  - Réponse : 200 — Listes
- **GET** /v1/price-lists/{id} — Détails d'une liste de prix
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/price-lists/{id} — Mettre à jour les prix
  - Requis : id
  - Réponse : 200 — Mis à jour
- **POST** /v1/price-lists/{id}/assign — Assigner une liste à un compte ou groupe
  - Requis : id
  - Réponse : 200 — Assignée
- **POST** /v1/price-lists/lookup — Prix effectif d'un produit pour un client donné
  - Requis : product_id, customer_id
  - Réponse : 200 — Prix effectif

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# pricing-api

**Titre** : Pricing API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Prix dynamiques et promotions. Calcul des remises, codes promo et règles tarifaires. DIFFÉRENCE vs discount-api : Pricing calcule le prix final d'un produit en tenant compte de toutes les règles, Discount gère uniquement les campagnes de codes promo.

## Endpoints
- **GET** /v1/pricing/product/{productId} — Prix actuel d'un produit
  - Requis : productId
  - Réponse : 200 — Prix
- **POST** /v1/pricing/calculate — Calculer le prix total d'un panier avec remises
  - Réponse : 200 — Prix calculé
- **POST** /v1/pricing/promo/validate — Valider un code promo
  - Requis : code, order_amount
  - Réponse : 200 — Valide — remise calculée | 400 — Code invalide ou expiré
- **GET** /v1/pricing/rules — Lister les règles tarifaires
  - Réponse : 200 — Règles
- **POST** /v1/pricing/rules — Créer une règle tarifaire
  - Réponse : 201 — Créée
- **PUT** /v1/pricing/rules/{id} — Mettre à jour une règle
  - Requis : id
  - Réponse : 200 — Mis à jour

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# privileged-access-api

**Titre** : Privileged Access API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Gestion accès privilégiés PAM. Coffre-fort mots de passe, sessions et enregistrement.

## Endpoints
- **GET** /v1/pam/credentials — Comptes privilégiés
  - Réponse : 200 — OK
- **POST** /v1/pam/credentials — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/pam/credentials/{id} — Emprunter credential
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/pam/credentials/{id} — Remettre
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/pam/sessions — Sessions privilégiées
  - Réponse : 200 — OK
- **POST** /v1/pam/sessions — Démarrer session
  - Réponse : 200 — OK
- **GET** /v1/pam/recordings — Enregistrements
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# product-api-v1

**Titre** : Product API
**Version** : v1 | **Statut** : deprecated
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Version initiale de l'API produits. DEPRECATED depuis 2022. ID entier, pas de variantes, images comme string simple. Migrer vers v2.

## Endpoints
- **GET** /v1/products — Lister les produits
  - Réponse : 200 — Liste
- **POST** /v1/products — Créer un produit
  - Réponse : 201 — Créé
- **GET** /v1/products/{id} — Récupérer un produit
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/products/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/products/{id} — Supprimer définitivement (BREAKING v2: devient archive)
  - Requis : id
  - Réponse : 204 — Supprimé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# product-api-v2

**Titre** : Product API
**Version** : v2 | **Statut** : deprecated
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Version 2 — DEPRECATED jan 2024. Introduit IDs préfixés PROD-, images multiples, variantes produit (taille/couleur) et structure pricing. Migrer vers v3.

## Endpoints
- **GET** /v2/products — Lister avec variantes
  - Réponse : 200 — Liste paginée
- **POST** /v2/products — Créer un produit avec variantes
  - Réponse : 201 — Créé
- **GET** /v2/products/{id} — Détails d'un produit
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v2/products/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v2/products/{id} — Archiver (soft delete)
  - Requis : id
  - Réponse : 200 — Archivé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# product-api-v3

**Titre** : Product API
**Version** : v3 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Version actuelle. Produits enrichis avec SEO, variantes en sous-ressource, category_id lié au catalogue et currency obligatoire. Recommandée pour tous les nouveaux développements.

## Endpoints
- **GET** /v3/products — Lister les produits avec SEO et filtres enrichis
  - Réponse : 200 — Liste paginée enrichie
- **POST** /v3/products — Créer un produit complet
  - Réponse : 201 — Créé | 422 — SEO manquant pour status=active
- **GET** /v3/products/{id} — Détails complets d'un produit
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v3/products/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v3/products/{id} — Archiver le produit
  - Requis : id
  - Réponse : 200 — Archivé
- **GET** /v3/products/{id}/variants — Variantes d'un produit
  - Requis : id
  - Réponse : 200 — Variantes
- **POST** /v3/products/{id}/variants — Ajouter une variante
  - Requis : id, sku, attributes
  - Réponse : 201 — Variante ajoutée
- **PUT** /v3/products/{id}/variants/{variantId} — Modifier une variante
  - Requis : id, variantId
  - Réponse : 200 — Mise à jour
- **DELETE** /v3/products/{id}/variants/{variantId} — Supprimer une variante
  - Requis : id, variantId
  - Réponse : 204 — Supprimée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# product-api-v4

**Titre** : Product API
**Version** : v4 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Version actuelle et recommandée de l'API Produit. Introduit la gestion multi-catalogue (B2B/B2C), les bundles natifs, l'IA de description automatique et la conformité PIM complète. DIFFÉRENCE vs product-catalog-api : Product API gère le cycle de vie complet (création, variantes, SEO, publication), Product Catalog API gère la taxonomie et les catégories.

## Endpoints
- **GET** /v4/products — Lister produits multi-catalogue avec filtres IA
  - Réponse : 200 — Liste paginée enrichie
- **POST** /v4/products — Créer un produit avec description IA optionnelle
  - Réponse : 201 — Produit créé | 422 — SEO manquant pour lifecycle_stage=active
- **GET** /v4/products/{id} — Produit complet avec structured data JSON-LD
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v4/products/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v4/products/{id} — Passer en end_of_life (jamais supprimé)
  - Requis : id
  - Réponse : 200 — Lifecycle → end_of_life
- **GET** /v4/products/{id}/variants — Variantes paginées (BREAKING: plus dans la réponse racine)
  - Requis : id
  - Réponse : 200 — Variantes
- **POST** /v4/products/{id}/variants — Ajouter une variante
  - Requis : id, sku, attributes
  - Réponse : 201 — Ajoutée
- **POST** /v4/products/{id}/ai-description — Générer une description produit par IA (nouveau en v4)
  - Requis : id
  - Réponse : 200 — Description générée

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# product-catalog-api-v1

**Titre** : Product Catalog API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Catalogue produits v1. DEPRECATED.

## Endpoints
- **GET** /v1/products — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# product-catalog-api-v2

**Titre** : Product Catalog API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Catalogue v2 avec variantes. DEPRECATED.

## Endpoints
- **GET** /v2/products — Lister
  - Réponse : 200 — OK
- **POST** /v2/products — Créer
  - Réponse : 200 — OK
- **GET** /v2/products/{id}/variants — Variantes
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# product-catalog-api-v3

**Titre** : Product Catalog API
**Version** : v3 | **Statut** : active
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Catalogue produits omnicanal. Variantes, prix, medias et SEO. DIFFERENCE vs inventory-api : Product Catalog = fiche produit et description, Inventory = stock disponible.

## Endpoints
- **GET** /v3/products — Catalogue
  - Réponse : 200 — OK
- **POST** /v3/products — Créer produit
  - Réponse : 200 — OK
- **GET** /v3/products/{id} — Fiche produit
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/products/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/products/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/products/{id}/variants — Variantes
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/products/{id}/variants — Ajouter variante
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/products/{id}/media — Medias
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/products/{id}/media — Ajouter media
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/products/search — Rechercher produits
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# product-catalog-api

**Titre** : Product Catalog API
**Version** : v2 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Catalogue produits. CRUD complet sur produits, catégories et attributs. DIFFÉRENCE vs search-api : Catalog = gestion des données produits, Search = interrogation du catalogue.

## Endpoints
- **GET** /v2/products — Lister les produits
  - Réponse : 200 — Produits
- **POST** /v2/products — Créer un produit
  - Requis : name, sku, price
  - Réponse : 201 — Créé
- **GET** /v2/products/{id} — Détails d'un produit
  - Requis : id
  - Réponse : 200 — Produit | 404 — 
- **PUT** /v2/products/{id} — Mettre à jour un produit
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v2/products/{id} — Archiver un produit
  - Requis : id
  - Réponse : 200 — Archivé
- **GET** /v2/categories — Lister les catégories
  - Réponse : 200 — Catégories
- **POST** /v2/categories — Créer une catégorie
  - Requis : name
  - Réponse : 201 — Créée

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# production-order-api-v1

**Titre** : Production Order API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Ordres de fabrication v1. DEPRECATED.

## Endpoints
- **GET** /v1/orders — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# production-order-api-v2

**Titre** : Production Order API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
OF v2 avec gammes. DEPRECATED.

## Endpoints
- **GET** /v2/orders — Lister
  - Réponse : 200 — OK
- **POST** /v2/orders — Creer
  - Réponse : 200 — OK
- **GET** /v2/orders/{id}/operations — Operations
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# production-order-api-v3

**Titre** : Production Order API
**Version** : v3 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Ordres de fabrication complets. Gammes, nomenclatures, suivi et tracing. DIFFERENCE vs order-management-api : Production Order = OF industriel avec gammes/ressources, Order Management = commande commerciale client.

## Endpoints
- **GET** /v3/orders — Ordres de fabrication
  - Réponse : 200 — OK
- **POST** /v3/orders — Creer OF
  - Réponse : 200 — OK
- **GET** /v3/orders/{id} — Detail OF
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/orders/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/orders/{id} — Cloturer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/orders/{id}/operations — Gamme
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/orders/{id}/operations — Ajouter operation
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/orders/{id}/materials — Nomenclature
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/orders/{id}/materials — Declarer consommation
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# production-planning-api

**Titre** : Production Planning API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Planification production. PDP, MPS et gestion capacite.

## Endpoints
- **GET** /v1/planning/pdp — Plan directeur
  - Réponse : 200 — OK
- **POST** /v1/planning/pdp — Mettre a jour PDP
  - Réponse : 200 — OK
- **GET** /v1/planning/capacity/{workcenter} — Plan capacite
  - Requis : workcenter
  - Réponse : 200 — OK
- **POST** /v1/planning/capacity/{workcenter} — Ajuster
  - Requis : workcenter
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# production-scheduling-api

**Titre** : Production Scheduling API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Ordonnancement production. Planning capacitaire, sequencement et optimisation.

## Endpoints
- **GET** /v1/scheduling/plan — Planning production
  - Réponse : 200 — OK
- **POST** /v1/scheduling/plan — Calculer ordonnancement
  - Réponse : 200 — OK
- **GET** /v1/scheduling/capacity — Charge capacitaire
  - Réponse : 200 — OK
- **POST** /v1/scheduling/capacity — Verifier capacite
  - Réponse : 200 — OK
- **GET** /v1/scheduling/jobs/{id} — Job ordonnance
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/scheduling/jobs/{id} — Reprogrammer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# profile-api

**Titre** : Profile API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Platform

## Description
Profil public et préférences d'expérience d'un utilisateur connecté. Avatar, bio, paramètres UI et préférences applicatives. DIFFÉRENCE vs user-api : Profile API = données d'affichage et préférences UX visibles par les autres (avatar, bio, timezone), User API = données d'identité et d'accès (email, mot de passe, rôles). DIFFÉRENCE vs customer-profile-api : Profile = préférences d'interface de n'importe quel utilisateur, Customer Profile = données commerciales d'un acheteur (segment, historique d'achat, fidélité).

## Endpoints
- **GET** /v1/profile/{userId} — Profil public d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Profil
- **PUT** /v1/profile/{userId} — Mettre à jour son profil
  - Requis : userId
  - Réponse : 200 — Mis à jour
- **PUT** /v1/profile/{userId}/avatar — Changer l'avatar
  - Requis : userId
  - Réponse : 200 — Avatar mis à jour — URL CDN retournée
- **DELETE** /v1/profile/{userId}/avatar — Supprimer l'avatar
  - Requis : userId
  - Réponse : 200 — Avatar supprimé
- **GET** /v1/profile/{userId}/preferences — Préférences applicatives
  - Requis : userId
  - Réponse : 200 — Préférences
- **PUT** /v1/profile/{userId}/preferences — Mettre à jour les préférences
  - Requis : userId
  - Réponse : 200 — Préférences mises à jour
- **GET** /v1/profile/{userId}/activity — Activité récente de l'utilisateur (connexions, actions)
  - Requis : userId
  - Réponse : 200 — Activité récente

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# project-api

**Titre** : Project API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Gestion de projets et sprints. Roadmaps, jalons, équipes et suivi budgétaire. DIFFÉRENCE vs task-api : Project est le conteneur qui structure les tâches en sprints et roadmap, Task est l'unité de travail individuelle. DIFFÉRENCE vs workflow-api : Project = gestion de projet humain avec planification, Workflow = orchestration d'automatisations techniques.

## Endpoints
- **POST** /v1/projects — Créer un projet
  - Réponse : 201 — Projet créé
- **GET** /v1/projects — Lister les projets
  - Réponse : 200 — Projets
- **GET** /v1/projects/{id} — Projet avec KPIs et avancement
  - Requis : id
  - Réponse : 200 — Projet | 404 — 
- **PUT** /v1/projects/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **GET** /v1/projects/{id}/sprints — Sprints du projet
  - Requis : id
  - Réponse : 200 — Sprints
- **POST** /v1/projects/{id}/sprints — Créer un sprint
  - Requis : id, name, start_date, end_date
  - Réponse : 201 — Sprint créé
- **GET** /v1/projects/{id}/milestones — Jalons et échéances
  - Requis : id
  - Réponse : 200 — Jalons
- **POST** /v1/projects/{id}/milestones — Créer un jalon
  - Requis : id, title, due_date
  - Réponse : 201 — Jalon créé
- **GET** /v1/projects/{id}/members — Membres du projet
  - Requis : id
  - Réponse : 200 — Membres
- **POST** /v1/projects/{id}/members — Ajouter un membre
  - Requis : id, user_id, role
  - Réponse : 201 — Ajouté

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# promotion-api

**Titre** : Promotion API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Marketing

## Description
Promotions commerciales automatiques. Remises sans code (ex: -20% sur toute la catégorie). DIFFÉRENCE vs discount-api : Promotion = remise automatique sans code (s'applique sur critères produits/segments), Discount = code promo saisi par l'utilisateur. DIFFÉRENCE vs pricing-api : Promotion crée les règles de remise, Pricing les applique au calcul final.

## Endpoints
- **POST** /v1/promotions — Créer une promotion automatique
  - Réponse : 201 — Créée
- **GET** /v1/promotions — Lister les promotions actives et planifiées
  - Réponse : 200 — Promotions
- **GET** /v1/promotions/{id} — Détails d'une promotion
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/promotions/{id} — Modifier une promotion
  - Requis : id
  - Réponse : 200 — Modifiée
- **PUT** /v1/promotions/{id}/activate — Activer
  - Requis : id
  - Réponse : 200 — Activée
- **PUT** /v1/promotions/{id}/deactivate — Désactiver
  - Requis : id
  - Réponse : 200 — Désactivée
- **POST** /v1/promotions/eligible — Promotions applicables à un panier donné
  - Requis : cart_id, customer_id
  - Réponse : 200 — Promotions éligibles

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# property-api-v1

**Titre** : Property API
**Version** : v1 | **Statut** : deprecated
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Biens immobiliers v1. DEPRECATED.

## Endpoints
- **GET** /v1/properties — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# property-api-v2

**Titre** : Property API
**Version** : v2 | **Statut** : deprecated
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Biens immobiliers v2 avec géolocalisation. DEPRECATED.

## Endpoints
- **GET** /v2/properties — Lister
  - Réponse : 200 — OK
- **POST** /v2/properties — Créer
  - Réponse : 200 — OK
- **GET** /v2/properties/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/properties/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# property-api-v3

**Titre** : Property API
**Version** : v3 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Biens immobiliers complets. Diagnostics DPE, photos 3D et valorisation IA. DIFFERENCE vs lease-api : Property = bien immobilier, Lease = contrat de bail sur ce bien.

## Endpoints
- **GET** /v3/properties — Lister biens
  - Réponse : 200 — OK
- **POST** /v3/properties — Créer bien
  - Réponse : 200 — OK
- **GET** /v3/properties/{id} — Detail complet
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/properties/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/properties/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/properties/{id}/valuation — Valorisation IA
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/properties/{id}/diagnostics — DPE et diagnostics
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/properties/{id}/diagnostics — Ajouter
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/properties/{id}/photos — Photos
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/properties/{id}/photos — Ajouter photo
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# property-inspection-api

**Titre** : Property Inspection API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
États des lieux et inspections. Entrée, sortie et périodiques.

## Endpoints
- **GET** /v1/inspections — Lister
  - Réponse : 200 — OK
- **POST** /v1/inspections — Créer etat des lieux
  - Réponse : 200 — OK
- **GET** /v1/inspections/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/inspections/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/inspections/{id} — Signer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/inspections/{id}/photos — Photos
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/inspections/{id}/photos — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# property-insurance-api

**Titre** : Property Insurance API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Assurance habitation et biens. MRH, garanties et sinistres. DIFFERENCE vs property-api (immobilier) : Property Insurance = contrat assurance bien, Property = fiche descriptive du bien.

## Endpoints
- **GET** /v1/property-insurance — Contrats habitation
  - Réponse : 200 — OK
- **POST** /v1/property-insurance — Souscrire MRH
  - Réponse : 200 — OK
- **GET** /v1/property-insurance/{contractId} — Detail contrat
  - Requis : contractId
  - Réponse : 200 — OK
- **PUT** /v1/property-insurance/{contractId} — Modifier
  - Requis : contractId
  - Réponse : 200 — OK
- **GET** /v1/property-insurance/{contractId}/guarantees — Garanties incluses
  - Requis : contractId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# property-management-api

**Titre** : Property Management API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion portefeuille immobilier. Vue consolidee, reporting et KPIs. DIFFERENCE vs property-api : Property Management = vue portefeuille multi-biens, Property = fiche d'un seul bien.

## Endpoints
- **GET** /v1/portfolio — Vue portefeuille
  - Réponse : 200 — OK
- **POST** /v1/portfolio — Ajouter bien
  - Réponse : 200 — OK
- **GET** /v1/portfolio/kpis — KPIs portefeuille
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# property-tax-api

**Titre** : Property Tax API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Taxes foncières et impositions immobilières. Calcul, déclarations et suivi.

## Endpoints
- **GET** /v1/property-tax/{propertyId} — Taxe fonciere
  - Requis : propertyId
  - Réponse : 200 — OK
- **POST** /v1/property-tax/{propertyId} — Calculer
  - Requis : propertyId
  - Réponse : 200 — OK
- **GET** /v1/property-tax/{propertyId}/declarations — Déclarations
  - Requis : propertyId
  - Réponse : 200 — OK
- **POST** /v1/property-tax/{propertyId}/declarations — Soumettre
  - Requis : propertyId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# provisioning-api

**Titre** : Provisioning API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Provisioning services telecom. Activation et deactivation lignes.

## Endpoints
- **POST** /v1/provisioning/activate — Activer
  - Réponse : 200 — OK
- **POST** /v1/provisioning/modify — Modifier
  - Réponse : 200 — OK
- **POST** /v1/provisioning/deactivate — Desactiver
  - Réponse : 200 — OK
- **GET** /v1/provisioning/status/{requestId} — Statut
  - Requis : requestId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# purchase-order-api

**Titre** : Purchase Order API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Supply

## Description
Bons de commande fournisseurs. Gestion des achats, réceptions et rapprochements. DIFFÉRENCE vs order-api : Purchase Order = commandes passées AUX fournisseurs (B2B achats), Order API = commandes passées PAR les clients (B2C ventes).

## Endpoints
- **POST** /v1/purchase-orders — Créer un bon de commande fournisseur
  - Réponse : 201 — Bon de commande créé
- **GET** /v1/purchase-orders — Lister les bons de commande
  - Réponse : 200 — Bons de commande
- **GET** /v1/purchase-orders/{id} — Détails d'un bon de commande
  - Requis : id
  - Réponse : 200 — Bon de commande
- **POST** /v1/purchase-orders/{id}/receive — Enregistrer une réception de marchandises
  - Requis : id
  - Réponse : 200 — Réception enregistrée — stock mis à jour

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# push-api

**Titre** : Push Notification API
**Version** : v1 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Notifications push mobiles iOS et Android. Tokens, segments et campagnes push. DIFFÉRENCE vs notification-api : Push API = canal mobile seul avec gestion device tokens et segments. Notification API = façade multi-canal. DIFFÉRENCE vs messaging-api : Push = unidirectionnel système→mobile, Messaging = bidirectionnel.

## Endpoints
- **POST** /v1/push/send — Envoyer une notification push
  - Réponse : 201 — Envoyée
- **POST** /v1/push/register-device — Enregistrer un device mobile
  - Requis : user_id, device_token, platform
  - Réponse : 201 — Enregistré
- **DELETE** /v1/push/unregister-device — Désenregistrer un device
  - Requis : device_token
  - Réponse : 204 — Désenregistré
- **POST** /v1/push/campaigns — Créer une campagne push
  - Requis : title, message, segment
  - Réponse : 201 — Créée
- **GET** /v1/push/campaigns/{id}/stats — Statistiques d'une campagne push
  - Requis : id
  - Réponse : 200 — Stats

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# quality-api

**Titre** : Quality Control API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Supply

## Description
Contrôle qualité des produits reçus. Inspections, non-conformités et réclamations fournisseurs.

## Endpoints
- **POST** /v1/quality/inspections — Créer un rapport d'inspection
  - Requis : purchase_order_id, inspector_id
  - Réponse : 201 — Rapport créé
- **GET** /v1/quality/inspections — Lister les inspections
  - Réponse : 200 — Inspections
- **GET** /v1/quality/non-conformities — Non-conformités en cours
  - Réponse : 200 — Non-conformités
- **POST** /v1/quality/non-conformities — Déclarer une non-conformité
  - Requis : product_id, type, description
  - Réponse : 201 — Non-conformité déclarée

## Authentification
ApiKeyAuth — apiKey

---

# quality-control-api

**Titre** : Quality Control API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Controle qualite production. Plans de controle, mesures et non-conformites. DIFFERENCE vs data-quality-api : Quality Control = qualite produit physique, Data Quality = qualite donnees informatiques.

## Endpoints
- **GET** /v1/quality/plans — Plans de controle
  - Réponse : 200 — OK
- **POST** /v1/quality/plans — Creer
  - Réponse : 200 — OK
- **GET** /v1/quality/checks/{orderId} — Controles
  - Requis : orderId
  - Réponse : 200 — OK
- **POST** /v1/quality/checks/{orderId} — Realiser controle
  - Requis : orderId
  - Réponse : 200 — OK
- **GET** /v1/quality/nonconformities — Non-conformites
  - Réponse : 200 — OK
- **POST** /v1/quality/nonconformities — Declarer NC
  - Réponse : 200 — OK
- **GET** /v1/quality/nonconformities/{id} — Detail NC
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/quality/nonconformities/{id} — Resoudre NC
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# queue-api

**Titre** : Queue API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Files d'attente de messages asynchrones. Publication, consommation et gestion des dead-letter queues.

## Endpoints
- **GET** /v1/queues — Lister les queues
  - Réponse : 200 — Queues
- **POST** /v1/queues — Créer une queue
  - Requis : name
  - Réponse : 201 — Créée
- **POST** /v1/queues/{name}/publish — Publier un message
  - Requis : name, body
  - Réponse : 201 — Publié
- **GET** /v1/queues/{name}/consume — Consommer des messages (max 10)
  - Requis : name
  - Réponse : 200 — Messages
- **DELETE** /v1/queues/{name}/messages/{id}/ack — Acquitter un message (le supprime de la queue)
  - Requis : name, id
  - Réponse : 204 — Acquitté
- **GET** /v1/queues/{name}/dlq — Messages en dead-letter queue (échecs après max_retries)
  - Requis : name
  - Réponse : 200 — Messages DLQ

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# r-and-d-api

**Titre** : R and D API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Recherche et developpement. Projets R&D, innovations et brevets.

## Endpoints
- **GET** /v1/rnd/projects — Projets
  - Réponse : 200 — OK
- **POST** /v1/rnd/projects — Creer projet
  - Réponse : 200 — OK
- **GET** /v1/rnd/projects/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/rnd/projects/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/rnd/projects/{id}/milestones — Jalons
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/rnd/projects/{id}/milestones — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# radiology-api

**Titre** : Radiology API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Imagerie médicale (radio, scanner, IRM). Planification examens, résultats DICOM et comptes-rendus.

## Endpoints
- **GET** /v1/imaging/orders — Demandes imagerie
  - Réponse : 200 — OK
- **POST** /v1/imaging/orders — Prescrire examen
  - Réponse : 200 — OK
- **GET** /v1/imaging/orders/{id} — Détail examen
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/imaging/orders/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/imaging/orders/{id}/results — Résultats DICOM
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/imaging/orders/{id}/results — Compte-rendu
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# rate-limit-api

**Titre** : Rate Limit API
**Version** : v1 | **Statut** : active
**Domaine** : Infrastructure | **Équipe** : Equipe Platform

## Description
Gestion des quotas et limites de débit par client et endpoint.

## Endpoints
- **GET** /v1/rate-limits/{clientId} — Quotas d'un client
  - Requis : clientId
  - Réponse : 200 — Quotas
- **PUT** /v1/rate-limits/{clientId} — Modifier les quotas d'un client
  - Requis : clientId
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/rate-limits/{clientId}/reset — Réinitialiser les compteurs
  - Requis : clientId
  - Réponse : 204 — Réinitialisé
- **POST** /v1/rate-limits/blacklist — Blacklister un IP ou client
  - Requis : type, value
  - Réponse : 201 — Blacklisté

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# rate-limiting-api

**Titre** : Rate Limiting API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Gestion quotas et rate limiting. Par client, endpoint et periode.

## Endpoints
- **GET** /v1/rate-limits — Quotas configures
  - Réponse : 200 — OK
- **POST** /v1/rate-limits — Creer quota
  - Réponse : 200 — OK
- **GET** /v1/rate-limits/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/rate-limits/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/rate-limits/check — Consommer quota
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# rating-api

**Titre** : Rating API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Notations numériques produits (1-5 étoiles). Scores moyens et distributions. DIFFÉRENCE vs review-api : Rating = note numérique seule, Review = texte complet + note. Cas d'usage : vote rapide sans rédiger un avis.

## Endpoints
- **POST** /v1/ratings — Soumettre une note
  - Requis : product_id, score, user_id
  - Réponse : 201 — Note enregistrée
- **GET** /v1/ratings/product/{productId} — Toutes les notes d'un produit
  - Requis : productId
  - Réponse : 200 — Notes
- **GET** /v1/ratings/average/{productId} — Moyenne des notes
  - Requis : productId
  - Réponse : 200 — Moyenne
- **GET** /v1/ratings/distribution/{productId} — Distribution des notes (1 à 5 étoiles)
  - Requis : productId
  - Réponse : 200 — Distribution

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# real-estate-search-api

**Titre** : Real Estate Search API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Recherche biens immobiliers. Filtres avancés, carte et alertes. DIFFERENCE vs search-api-v3 : Real Estate Search = recherche biens immobiliers spécifiquement, Search = moteur de recherche générique.

## Endpoints
- **GET** /v1/real-estate/search — Rechercher biens
  - Réponse : 200 — OK
- **POST** /v1/real-estate/search — Sauvegarder recherche
  - Réponse : 200 — OK
- **GET** /v1/real-estate/alerts — Alertes actives
  - Réponse : 200 — OK
- **POST** /v1/real-estate/alerts — Créer alerte
  - Réponse : 200 — OK
- **GET** /v1/real-estate/map — Biens sur carte
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# real-estate-valuation-api

**Titre** : Real Estate Valuation API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Valorisation immobilière par IA. Estimation, comparables et tendances. DIFFERENCE vs property-api : Valuation = estimation valeur marché, Property = fiche descriptive du bien.

## Endpoints
- **POST** /v1/valuation/estimate — Estimer valeur marche
  - Réponse : 200 — OK
- **GET** /v1/valuation/{propertyId} — Valorisation bien
  - Requis : propertyId
  - Réponse : 200 — OK
- **POST** /v1/valuation/comparables — Biens comparables
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# recommendation-api

**Titre** : Recommendation API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Data

## Description
Recommandations personnalisées de produits. Collaboratif et basé sur le contenu.

## Endpoints
- **GET** /v1/recommendations/{userId} — Recommandations personnalisées pour un utilisateur
  - Requis : userId
  - Réponse : 200 — Produits recommandés
- **GET** /v1/recommendations/similar/{productId} — Produits similaires
  - Requis : productId
  - Réponse : 200 — Produits similaires
- **GET** /v1/recommendations/trending — Produits tendance
  - Réponse : 200 — Tendances
- **POST** /v1/recommendations/feedback — Feedback sur une recommandation (clic, achat, rejet)
  - Requis : user_id, product_id, action
  - Réponse : 202 — Feedback enregistré

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# recruitment-api

**Titre** : Recruitment API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Recrutement et candidatures. Offres d'emploi, candidats et processus de sélection.

## Endpoints
- **POST** /v1/jobs — Publier une offre d'emploi
  - Requis : title, department, contract_type
  - Réponse : 201 — Offre publiée
- **GET** /v1/jobs — Lister les offres d'emploi
  - Réponse : 200 — Offres
- **POST** /v1/jobs/{id}/apply — Postuler à une offre
  - Requis : id, full_name, email
  - Réponse : 201 — Candidature reçue
- **GET** /v1/jobs/{id}/candidates — Candidats pour une offre
  - Requis : id
  - Réponse : 200 — Candidats
- **PUT** /v1/candidates/{id}/status — Mettre à jour le statut d'un candidat
  - Requis : id, status
  - Réponse : 200 — Mis à jour

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# referral-api

**Titre** : Referral API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe Marketing

## Description
Programme de parrainage. Codes de référence, tracking et récompenses.

## Endpoints
- **POST** /v1/referrals/generate — Générer un code de parrainage
  - Requis : user_id
  - Réponse : 201 — Code généré
- **GET** /v1/referrals/{code} — Détails d'un code de parrainage
  - Requis : code
  - Réponse : 200 — Parrainage
- **POST** /v1/referrals/validate — Valider un parrainage lors d'une inscription
  - Requis : code, new_user_id
  - Réponse : 200 — Validé — récompenses attribuées
- **GET** /v1/referrals/{userId}/stats — Statistiques de parrainage d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Stats

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# referral-health-api

**Titre** : Referral Health API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Orientations entre professionnels de santé. Consultations spécialisées et lettres de liaison. DIFFÉRENCE vs referral-api (e-commerce) : Referral Health = orientation médicale, Referral = parrainage client.

## Endpoints
- **GET** /v1/referrals — Demandes orientation
  - Réponse : 200 — OK
- **POST** /v1/referrals — Créer orientation
  - Réponse : 200 — OK
- **GET** /v1/referrals/{id} — Détail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/referrals/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/referrals/{id}/letter — Lettre de liaison
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/referrals/{id}/letter — Générer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# regulatory-reporting-api

**Titre** : Regulatory Reporting API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Reporting reglementaire obligatoire. AMF, ACPR, DGFiP et soumissions automatisees.

## Endpoints
- **GET** /v1/regulatory/reports — Rapports reglementaires
  - Réponse : 200 — OK
- **POST** /v1/regulatory/reports — Créer rapport
  - Réponse : 200 — OK
- **GET** /v1/regulatory/reports/{id} — Statut soumission
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/regulatory/reports/{id} — Soumettre au régulateur
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/regulatory/deadlines — Échéances réglementaires
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# reinsurance-api

**Titre** : Reinsurance API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Réassurance et cession de risques. Traités, facultatives et sinistres réassureurs.

## Endpoints
- **GET** /v1/reinsurance/treaties — Traités de réassurance
  - Réponse : 200 — OK
- **POST** /v1/reinsurance/treaties — Créer traité
  - Réponse : 200 — OK
- **GET** /v1/reinsurance/treaties/{id} — Detail traité
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/reinsurance/treaties/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/reinsurance/claims — Sinistres cédés
  - Réponse : 200 — OK
- **POST** /v1/reinsurance/claims — Céder sinistre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# renewable-api

**Titre** : Renewable Energy API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Gestion sources d'énergie renouvelable. Solaire, éolien, hydraulique et mix énergétique.

## Endpoints
- **GET** /v1/renewable/sources — Sources renouvelables
  - Réponse : 200 — OK
- **POST** /v1/renewable/sources — Ajouter source
  - Réponse : 200 — OK
- **GET** /v1/renewable/sources/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/renewable/mix — Prévision mix
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# renewal-api

**Titre** : Renewal API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Renouvellements contrats. Notifications, négociation et confirmation.

## Endpoints
- **GET** /v1/renewals — Renouvellements à venir
  - Réponse : 200 — OK
- **POST** /v1/renewals — Traiter renouvellement
  - Réponse : 200 — OK
- **GET** /v1/renewals/{contractId} — Statut renouvellement
  - Requis : contractId
  - Réponse : 200 — OK
- **POST** /v1/renewals/{contractId} — Négocier conditions
  - Requis : contractId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# renovation-api

**Titre** : Renovation API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion travaux de rénovation. Devis, planning et suivi chantier.

## Endpoints
- **GET** /v1/renovations — Projets en cours
  - Réponse : 200 — OK
- **POST** /v1/renovations — Créer projet
  - Réponse : 200 — OK
- **GET** /v1/renovations/{id} — Detail projet
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/renovations/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/renovations/{id}/quotes — Devis
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/renovations/{id}/quotes — Ajouter devis
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/renovations/{id}/progress — Avancement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/renovations/{id}/progress — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# rent-collection-api

**Titre** : Rent Collection API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Collecte loyers et charges. Quittances, relances et comptabilité. DIFFERENCE vs billing-api : Rent Collection = loyers immobiliers avec quittances, Billing = abonnements et facturation générique.

## Endpoints
- **GET** /v1/rent/{leaseId} — Statut loyer
  - Requis : leaseId
  - Réponse : 200 — OK
- **POST** /v1/rent/{leaseId} — Enregistrer paiement
  - Requis : leaseId
  - Réponse : 200 — OK
- **GET** /v1/rent/{leaseId}/receipts — Quittances
  - Requis : leaseId
  - Réponse : 200 — OK
- **POST** /v1/rent/{leaseId}/receipts — Générer quittance
  - Requis : leaseId
  - Réponse : 200 — OK
- **GET** /v1/rent/{leaseId}/reminders — Relances
  - Requis : leaseId
  - Réponse : 200 — OK
- **POST** /v1/rent/{leaseId}/reminders — Envoyer relance
  - Requis : leaseId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# report-api

**Titre** : Report API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Rapport spécifique à une ressource métier — vue synthétique d'une entité (commande, client, projet). Génère un rapport contextuel sur demande. DIFFÉRENCE vs reporting-api : Reporting API génère des rapports périodiques planifiés sur des populations de données (ex: rapport mensuel des ventes), Report API génère un rapport contextuel instantané sur une ressource spécifique (ex: rapport de la commande ORD-0042). DIFFÉRENCE vs analytics-api : Analytics = exploration interactive de métriques agrégées, Report = document de synthèse sur une entité précise.

## Endpoints
- **GET** /v1/report/{resourceType}/{resourceId} — Générer un rapport contextuel sur une ressource
  - Requis : resourceType, resourceId
  - Réponse : 200 — Rapport complet de la ressource
- **POST** /v1/report/batch — Générer plusieurs rapports en une fois
  - Requis : resources
  - Réponse : 202 — Génération asynchrone — zip retourné
- **GET** /v1/report/templates — Templates de rapport disponibles par type de ressource
  - Réponse : 200 — Templates
- **POST** /v1/report/templates — Créer un template de rapport custom
  - Requis : name, resource_type, sections
  - Réponse : 201 — Template créé
- **POST** /v1/report/scheduled — Planifier un rapport récurrent sur une ressource
  - Requis : resource_type, resource_id, cron, recipients
  - Réponse : 201 — Rapport planifié

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# reporting-api-v2

**Titre** : Reporting API
**Version** : v2 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Version 2 Reporting. Rapports interactifs HTML, white-labeling et collaboration. DIFFÉRENCE vs v1 : ajout format HTML interactif, personnalisation logo/couleurs et commentaires sur rapports.

## Endpoints
- **POST** /v2/reports/generate — Générer un rapport avec options white-label
  - Requis : type, format
  - Réponse : 202 — Génération lancée
- **POST** /v2/reports/{id}/comments — Ajouter un commentaire collaboratif
  - Requis : id, content
  - Réponse : 201 — Commentaire ajouté
- **POST** /v2/reports/{id}/share — Partager un rapport avec un lien externe
  - Requis : id
  - Réponse : 200 — Lien de partage

## Authentification
ApiKeyAuth — apiKey

---

# reporting-api

**Titre** : Reporting API
**Version** : v1 | **Statut** : active
**Domaine** : Analytics & BI | **Équipe** : Equipe Data

## Description
Génération de rapports planifiés. Export PDF, Excel, tableaux de bord programmés. DIFFÉRENCE vs analytics-api : Reporting = documents générés et envoyés par email, Analytics = métriques consultables en temps réel.

## Endpoints
- **POST** /v1/reports/generate — Générer un rapport
  - Requis : type, format
  - Réponse : 202 — Génération lancée
- **GET** /v1/reports/{id} — Statut de génération
  - Requis : id
  - Réponse : 200 — Statut
- **GET** /v1/reports/{id}/download — Télécharger le rapport
  - Requis : id
  - Réponse : 200 — Fichier
- **POST** /v1/reports/schedule — Planifier un rapport récurrent
  - Réponse : 201 — Planifié
- **GET** /v1/reports/templates — Modèles de rapports disponibles
  - Réponse : 200 — Templates

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# restaurant-reservation-api

**Titre** : Restaurant Reservation API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Réservations restaurant. Tables, menus et listes d'attente.

## Endpoints
- **GET** /v1/reservations — Réservations du jour
  - Réponse : 200 — OK
- **POST** /v1/reservations — Réserver table
  - Réponse : 200 — OK
- **GET** /v1/reservations/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/reservations/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/reservations/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/waitlist — File d'attente
  - Réponse : 200 — OK
- **POST** /v1/waitlist — S'inscrire liste
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# return-api

**Titre** : Return API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Commerce

## Description
Retours produits et remboursements. Demandes, validation, suivi et logistique inverse.

## Endpoints
- **POST** /v1/returns — Créer une demande de retour
  - Requis : order_id, items, reason
  - Réponse : 201 — Demande créée
- **GET** /v1/returns/{id} — Statut d'une demande de retour
  - Requis : id
  - Réponse : 200 — Retour
- **PUT** /v1/returns/{id}/approve — Approuver le retour
  - Requis : id
  - Réponse : 200 — Approuvé
- **PUT** /v1/returns/{id}/reject — Rejeter la demande de retour
  - Requis : id, reason
  - Réponse : 200 — Rejeté
- **GET** /v1/returns?orderId={id} — Retours d'une commande
  - Requis : orderId
  - Réponse : 200 — Retours

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# returns-api

**Titre** : Returns API
**Version** : v1 | **Statut** : active
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Retours et remboursements. SAV, labels retour et reintegration stock.

## Endpoints
- **GET** /v1/returns — Retours en cours
  - Réponse : 200 — OK
- **POST** /v1/returns — Initier retour
  - Réponse : 200 — OK
- **GET** /v1/returns/{id} — Detail retour
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/returns/{id} — Mettre a jour statut
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/returns/{id}/label — Label retour
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/returns/{id}/label — Générer
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/returns/{id}/refund — Traiter remboursement
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# review-api

**Titre** : Review API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Catalog

## Description
Avis textuels et notations produits. Soumission, modération et agrégation des reviews clients. DIFFÉRENCE vs rating-api : Review contient le texte complet et la note, Rating gère uniquement la note numérique sans texte.

## Endpoints
- **POST** /v1/reviews — Soumettre un avis produit
  - Réponse : 201 — Avis soumis — en attente de modération
- **GET** /v1/reviews/product/{productId} — Avis d'un produit
  - Requis : productId
  - Réponse : 200 — Avis
- **DELETE** /v1/reviews/product/{productId} — Supprimer tous les avis d'un produit (admin)
  - Requis : productId
  - Réponse : 204 — Supprimés
- **PUT** /v1/reviews/{id}/moderate — Modérer un avis (approuver/rejeter)
  - Requis : id, action
  - Réponse : 200 — Modéré
- **DELETE** /v1/reviews/{id} — Supprimer un avis
  - Requis : id
  - Réponse : 204 — Supprimé
- **GET** /v1/reviews/stats/{productId} — Statistiques des avis d'un produit
  - Requis : productId
  - Réponse : 200 — Stats

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# risk-management-api

**Titre** : Risk Management API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Gestion risques cybersécurité. Identification, évaluation et traitement.

## Endpoints
- **GET** /v1/risks — Risques identifiés
  - Réponse : 200 — OK
- **POST** /v1/risks — Créer risque
  - Réponse : 200 — OK
- **GET** /v1/risks/{id} — Detail risque
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/risks/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/risks/{id}/treatment — Plan traitement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/risks/{id}/treatment — Appliquer traitement
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/risks/heatmap — Cartographie risques
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# risk-scoring-api

**Titre** : Risk Scoring API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Scoring risque assurance. Modèles actuariels et ML. DIFFERENCE vs credit-scoring-api : Risk Scoring = risque assurable (santé, auto, habitation), Credit Scoring = risque crédit bancaire.

## Endpoints
- **POST** /v1/risk/score — Calculer score risque
  - Réponse : 200 — OK
- **GET** /v1/risk/{clientId} — Score risque client
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/risk/models — Modèles disponibles
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# roaming-api

**Titre** : Roaming API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Roaming international. Accords, tarifs et consommation.

## Endpoints
- **GET** /v1/roaming/{subscriberId} — Statut
  - Requis : subscriberId
  - Réponse : 200 — OK
- **POST** /v1/roaming/{subscriberId} — Activer
  - Requis : subscriberId
  - Réponse : 200 — OK
- **DELETE** /v1/roaming/{subscriberId} — Desactiver
  - Requis : subscriberId
  - Réponse : 200 — OK
- **GET** /v1/roaming/{subscriberId}/usage — Consommation
  - Requis : subscriberId
  - Réponse : 200 — OK
- **GET** /v1/roaming/agreements — Accords
  - Réponse : 200 — OK
- **POST** /v1/roaming/agreements — Ajouter
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# room-booking-api-v1

**Titre** : Room Booking API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Réservation chambres v1. DEPRECATED.

## Endpoints
- **POST** /v1/bookings — Réserver
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# room-booking-api-v2

**Titre** : Room Booking API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Réservation chambres v2. DEPRECATED.

## Endpoints
- **GET** /v2/bookings — Lister
  - Réponse : 200 — OK
- **POST** /v2/bookings — Réserver
  - Réponse : 200 — OK
- **GET** /v2/bookings/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/bookings/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# room-booking-api-v3

**Titre** : Room Booking API
**Version** : v3 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Réservation chambres avec garanties et politiques annulation. DIFFERENCE vs amenity-booking-api : Room Booking = chambre d'hôtel, Amenity Booking = équipements résidentiels partagés.

## Endpoints
- **GET** /v3/bookings — Réservations
  - Réponse : 200 — OK
- **POST** /v3/bookings — Réserver chambre
  - Réponse : 200 — OK
- **GET** /v3/bookings/{id} — Detail réservation
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/bookings/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/bookings/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/bookings/{id}/payment — Rembourser
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/bookings/check-availability — Vérifier disponibilité
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# route-optimization-api

**Titre** : Route Optimization API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Optimisation itinéraires et tournées. VRP multi-contraintes et réoptimisation dynamique.

## Endpoints
- **POST** /v1/routes/optimize — Optimiser tournée
  - Réponse : 200 — OK
- **GET** /v1/routes/{id} — Itinéraire calculé
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/routes/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# sanctions-screening-api

**Titre** : Sanctions Screening API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Criblage listes sanctions internationales. UE, OFAC, ONU et gel avoirs.

## Endpoints
- **POST** /v1/sanctions/screen — Criblage en masse
  - Réponse : 200 — OK
- **GET** /v1/sanctions/lists — Dernière mise a jour
  - Réponse : 200 — OK
- **GET** /v1/sanctions/alerts — Alertes criblage
  - Réponse : 200 — OK
- **PUT** /v1/sanctions/alerts — Résoudre alerte
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# savings-api

**Titre** : Savings API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Comptes epargne (Livret A, LDDS, PEL). Taux, plafonds et versements programmes.

## Endpoints
- **GET** /v1/savings/{clientId} — Livrets du client
  - Requis : clientId
  - Réponse : 200 — OK
- **POST** /v1/savings/{clientId} — Ouvrir livret
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/savings/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/savings/{id} — Versement
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# scada-api

**Titre** : SCADA API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
SCADA supervision industrielle. Acquisition donnees terrain et telecommande.

## Endpoints
- **GET** /v1/scada/tags — Tags SCADA
  - Réponse : 200 — OK
- **POST** /v1/scada/tags — Ajouter tag
  - Réponse : 200 — OK
- **GET** /v1/scada/tags/{id} — Valeur temps reel
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/scada/tags/{id} — Ecrire valeur
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/scada/alarms — Alarmes actives
  - Réponse : 200 — OK
- **PUT** /v1/scada/alarms — Effacer
  - Réponse : 200 — OK
- **POST** /v1/scada/historian — Interroger historique
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# scheduler-api

**Titre** : Scheduler API
**Version** : v1 | **Statut** : active
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Planification taches. CRON, one-shot et gestion erreurs.

## Endpoints
- **GET** /v1/scheduler/jobs — Jobs planifies
  - Réponse : 200 — OK
- **POST** /v1/scheduler/jobs — Planifier job
  - Réponse : 200 — OK
- **GET** /v1/scheduler/jobs/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/scheduler/jobs/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/scheduler/jobs/{id} — Supprimer
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/scheduler/jobs/{id} — Executer maintenant
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/scheduler/jobs/{id}/history — Historique executions
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# scholarship-api

**Titre** : Scholarship API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Bourses et aides financières. Candidatures, critères et versements.

## Endpoints
- **GET** /v1/scholarships — Bourses disponibles
  - Réponse : 200 — OK
- **POST** /v1/scholarships — Candidater
  - Réponse : 200 — OK
- **GET** /v1/scholarships/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/scholarships/{id} — Instruire dossier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/scholarships/student/{studentId} — Bourses étudiant
  - Requis : studentId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# search-api-v1

**Titre** : Search API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Cross | **Équipe** : Equipe Divers

## Description
Moteur recherche v1. DEPRECATED.

## Endpoints
- **GET** /v1/search — Rechercher
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# search-api-v2

**Titre** : Search API
**Version** : v2 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Platform

## Description
Version 2 Search. Recherche sémantique vectorielle, personnalisation par profil et A/B sur le ranking. DIFFÉRENCE vs v1 : v2 ajoute embedding vectoriel, personnalisation et expérimentation sur les résultats.

## Endpoints
- **GET** /v2/search — Recherche hybride (lexical + sémantique)
  - Requis : q
  - Réponse : 200 — Résultats personnalisés
- **POST** /v2/search/similar — Recherche par similarité (more-like-this)
  - Requis : reference_id
  - Réponse : 200 — Produits similaires
- **POST** /v2/search/reindex — Forcer une réindexation complète ou partielle
  - Réponse : 202 — Réindexation lancée

## Authentification
ApiKeyAuth — apiKey

---

# search-api-v3

**Titre** : Search API
**Version** : v3 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Platform

## Description
Version actuelle. Introduit la recherche conversationnelle (LLM), les synonymes configurables, le merchandising et le ranking A/B en production. DIFFÉRENCE vs search-api-v2 : v3 ajoute la couche LLM pour les requêtes en langage naturel et le merchandising manuel.

## Endpoints
- **GET** /v3/search — Recherche hybride + LLM conversationnelle
  - Requis : q
  - Réponse : 200 — Résultats avec explication optionnelle
- **POST** /v3/search/synonyms — Créer un dictionnaire de synonymes (nouveau en v3)
  - Requis : name, synonyms
  - Réponse : 201 — Dictionnaire créé
- **GET** /v3/search/synonyms — Lister les dictionnaires
  - Réponse : 200 — Dictionnaires
- **POST** /v3/search/merchandising — Créer règle de merchandising (boost/bury — nouveau en v3)
  - Requis : query_pattern, action
  - Réponse : 201 — Règle créée
- **GET** /v3/search/analytics — Analytics de recherche (requêtes sans résultat, taux de clic)
  - Réponse : 200 — Analytics de recherche

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# search-api

**Titre** : Search API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Platform

## Description
Recherche full-text sur le catalogue produits et commandes. Filtres, facettes et tri par pertinence. DIFFÉRENCE vs product-catalog-api : Search interroge les données, Product Catalog les gère.

## Endpoints
- **GET** /v1/search — Recherche globale
  - Requis : q
  - Réponse : 200 — Résultats
- **GET** /v1/search/products — Recherche produits avec facettes
  - Réponse : 200 — Produits
- **POST** /v1/search/advanced — Recherche avancée avec filtres complexes
  - Réponse : 200 — Résultats avancés
- **GET** /v1/search/suggestions — Autocomplétion et suggestions
  - Requis : q
  - Réponse : 200 — Suggestions

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# secret-api

**Titre** : Secret Manager API
**Version** : v1 | **Statut** : active
**Domaine** : Security & Compliance | **Équipe** : Equipe Security

## Description
Gestionnaire de secrets. Credentials, tokens et certificats stockés de manière sécurisée. DIFFÉRENCE vs api-key-api : Secret Manager = stockage générique de tous types de secrets (mots de passe, certificats, tokens tiers), API Key API = gestion spécifique des clés d'accès à nos APIs.

## Endpoints
- **POST** /v1/secrets — Créer un secret
  - Requis : name, value
  - Réponse : 201 — Secret créé (valeur non retournée)
- **GET** /v1/secrets — Lister les secrets (métadonnées uniquement)
  - Réponse : 200 — Secrets sans valeurs
- **GET** /v1/secrets/{name} — Lire la valeur d'un secret
  - Requis : name
  - Réponse : 200 — Secret avec valeur | 403 — Accès non autorisé
- **PUT** /v1/secrets/{name} — Mettre à jour la valeur
  - Requis : name, value
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/secrets/{name} — Supprimer un secret
  - Requis : name
  - Réponse : 204 — Supprimé
- **GET** /v1/secrets/{name}/versions — Historique des versions d'un secret
  - Requis : name
  - Réponse : 200 — Versions

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# security-incident-api-v1

**Titre** : Security Incident API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Incidents sécurité v1. DEPRECATED.

## Endpoints
- **GET** /v1/incidents — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# security-incident-api-v2

**Titre** : Security Incident API
**Version** : v2 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Gestion incidents sécurité. Detection, triage, investigation et clôture. DIFFERENCE vs vulnerability-api : Security Incident = attaque active en cours, Vulnerability = faille passive non exploitée.

## Endpoints
- **GET** /v2/incidents — Incidents en cours
  - Réponse : 200 — OK
- **POST** /v2/incidents — Déclarer incident
  - Réponse : 200 — OK
- **GET** /v2/incidents/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/incidents/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/incidents/{id}/timeline — Chronologie
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/incidents/{id}/timeline — Ajouter événement
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/incidents/{id}/response — Plan de réponse
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/incidents/{id}/response — Exécuter action
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# segmentation-api

**Titre** : Segmentation API
**Version** : v1 | **Statut** : active
**Domaine** : CRM & Marketing | **Équipe** : Equipe CRM

## Description
Segmentation dynamique des clients. Règles comportementales et attributs pour ciblage.

## Endpoints
- **POST** /v1/segments — Créer un segment
  - Requis : name, rules
  - Réponse : 201 — Créé
- **GET** /v1/segments — Lister les segments
  - Réponse : 200 — Segments
- **GET** /v1/segments/{id}/members — Membres d'un segment
  - Requis : id
  - Réponse : 200 — Membres
- **PUT** /v1/segments/{id}/rules — Mettre à jour les règles de segmentation
  - Requis : id
  - Réponse : 200 — Règles mises à jour
- **POST** /v1/segments/preview — Prévisualiser un segment avant création
  - Réponse : 200 — Aperçu — nombre de membres estimé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# sensor-data-api-v1

**Titre** : Sensor Data API
**Version** : v1 | **Statut** : deprecated
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Donnees capteurs v1. DEPRECATED.

## Endpoints
- **GET** /v1/sensors — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# sensor-data-api-v2

**Titre** : Sensor Data API
**Version** : v2 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Collecte et analyse données capteurs IoT. Températures, pression, humidité et vibrations. DIFFERENCE vs telemetry-api : Sensor Data = données brutes capteurs physiques, Telemetry = données agrégées équipements.

## Endpoints
- **GET** /v2/sensors — Lister capteurs
  - Réponse : 200 — OK
- **POST** /v2/sensors — Enregistrer capteur
  - Réponse : 200 — OK
- **GET** /v2/sensors/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/sensors/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/sensors/{id}/data — Données temps reel
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/sensors/{id}/data — Ingérer mesure
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/sensors/{id}/stream — Stream SSE temps reel
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# service-assurance-api

**Titre** : Service Assurance API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Assurance service telecom. SLA, incidents et resolution.

## Endpoints
- **GET** /v1/assurance/sla — Conformite SLA
  - Réponse : 200 — OK
- **POST** /v1/assurance/sla — Ouvrir violation
  - Réponse : 200 — OK
- **GET** /v1/assurance/incidents — Incidents
  - Réponse : 200 — OK
- **POST** /v1/assurance/incidents — Creer
  - Réponse : 200 — OK
- **GET** /v1/assurance/incidents/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/assurance/incidents/{id} — Resoudre
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# session-api

**Titre** : Session API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Gestion des sessions actives. Liste, révocation et détection de sessions suspectes. DIFFÉRENCE vs auth-api : Session API consulte et révoque les sessions existantes, Auth API les crée.

## Endpoints
- **GET** /v1/sessions/{userId} — Sessions actives d'un utilisateur
  - Requis : userId
  - Réponse : 200 — Sessions
- **DELETE** /v1/sessions/{sessionId} — Révoquer une session spécifique
  - Requis : sessionId
  - Réponse : 204 — Révoquée
- **DELETE** /v1/sessions/{userId}/revoke-all — Révoquer toutes les sessions (déconnexion totale)
  - Requis : userId
  - Réponse : 204 — Toutes révoquées
- **GET** /v1/sessions/suspicious — Sessions suspectes détectées (géoloc inhabituelle, IP blacklistée)
  - Réponse : 200 — Sessions suspectes

## Authentification
ApiKeyAuth — apiKey

---

# shipping-api-v1

**Titre** : Shipping API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Retail | **Équipe** : Equipe Retail

## Description
Expedition colis v1. DEPRECATED.

## Endpoints
- **POST** /v1/shipments — Expedier
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# shipping-api-v2

**Titre** : Shipping API
**Version** : v2 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Version 2 de l'API d'expédition — version actuelle recommandée. Ajout du tracking temps réel GPS, des expéditions multi-colis, de la gestion des douanes pour l'export international et du calcul CO2. DIFFÉRENCE vs delivery-api : Shipping gère les colis et transporteurs, Delivery gère les créneaux et plannings de livraison.

## Endpoints
- **POST** /v2/shipping/create — Créer expédition multi-colis avec calcul CO2 et douanes
  - Réponse : 201 — Expédition créée — étiquettes générées
- **POST** /v2/shipping/estimate — Estimer frais et CO2 par transporteur
  - Requis : parcels, destination
  - Réponse : 200 — Estimations avec CO2 par transporteur
- **GET** /v2/shipping/{id} — Statut complet de l'expédition
  - Requis : id
  - Réponse : 200 — Expédition
- **GET** /v2/shipping/{id}/live-track — Tracking GPS temps réel (WebSocket SSE — nouveau en v2)
  - Requis : id
  - Réponse : 200 — Stream SSE avec position GPS
- **GET** /v2/shipping/{id}/labels — Étiquettes en PDF ou ZPL (nouveau format en v2)
  - Requis : id
  - Réponse : 200 — Étiquettes
- **PUT** /v2/shipping/{id}/cancel — Annuler une expédition
  - Requis : id
  - Réponse : 200 — Annulée | 409 — 

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# shipping-api

**Titre** : Shipping API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Expéditions et livraisons. Calcul des frais de port, tracking et retours. DIFFÉRENCE vs delivery-api : Shipping gère les colis et transporteurs, Delivery gère les créneaux de livraison planifiés.

## Endpoints
- **POST** /v1/shipping/estimate — Estimer les frais de livraison
  - Requis : weight, destination
  - Réponse : 200 — Estimations par transporteur
- **POST** /v1/shipping/create — Créer une expédition
  - Requis : order_id, carrier, destination
  - Réponse : 201 — Expédition créée — étiquette générée
- **GET** /v1/shipping/{trackingId} — Suivre un colis
  - Requis : trackingId
  - Réponse : 200 — Statut de suivi
- **PUT** /v1/shipping/{trackingId}/cancel — Annuler une expédition
  - Requis : trackingId
  - Réponse : 200 — Annulée | 409 — 
- **POST** /v1/shipping/return — Créer un retour colis
  - Requis : order_id, reason
  - Réponse : 201 — Retour créé — étiquette retour générée

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# siem-api

**Titre** : SIEM API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Security Information and Event Management. Collecte logs, corrélation et alertes.

## Endpoints
- **GET** /v1/siem/events — Événements sécurité
  - Réponse : 200 — OK
- **POST** /v1/siem/events — Ingérer événement
  - Réponse : 200 — OK
- **GET** /v1/siem/rules — Règles corrélation
  - Réponse : 200 — OK
- **POST** /v1/siem/rules — Ajouter règle
  - Réponse : 200 — OK
- **GET** /v1/siem/alerts — Alertes SIEM
  - Réponse : 200 — OK
- **PUT** /v1/siem/alerts — Résoudre alerte
  - Réponse : 200 — OK
- **GET** /v1/siem/dashboards — Tableau de bord
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# smart-lock-api

**Titre** : Smart Lock API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Serrures connectées. Accès, codes temporaires et historique.

## Endpoints
- **GET** /v1/locks — Lister serrures
  - Réponse : 200 — OK
- **POST** /v1/locks — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/locks/{id} — Statut serrure
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/locks/{id} — Fermer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/locks/{id}/access-codes — Codes d'accès
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/locks/{id}/access-codes — Générer code temporaire
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/locks/{id}/access-codes — Révoquer
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# smart-meter-api-v1

**Titre** : Smart Meter API
**Version** : v1 | **Statut** : deprecated
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Compteurs intelligents v1. DEPRECATED.

## Endpoints
- **GET** /v1/meters — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# smart-meter-api-v2

**Titre** : Smart Meter API
**Version** : v2 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Compteurs intelligents eau/gaz/electricite avec relevé temps réel et alertes. DIFFERENCE vs water-meter-api : Smart Meter = multi-fluides, Water Meter = eau uniquement.

## Endpoints
- **GET** /v2/meters — Lister compteurs
  - Réponse : 200 — OK
- **POST** /v2/meters — Enregistrer
  - Réponse : 200 — OK
- **GET** /v2/meters/{id} — Releve temps reel
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/meters/{id}/history — Historique consommation
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/meters/{id}/alerts — Alertes
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/meters/{id}/alerts — Configurer seuil
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# sms-api

**Titre** : SMS API
**Version** : v1 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Envoi de SMS transactionnels et OTP. Canal SMS seul. DIFFÉRENCE vs notification-api : SMS API = canal SMS avec numéros courts dédiés, Notification API = façade multi-canal. DIFFÉRENCE vs messaging-api : SMS = externe vers mobile, Messaging = chat in-app bidirectionnel.

## Endpoints
- **POST** /v1/sms/send — Envoyer un SMS transactionnel
  - Réponse : 201 — Envoyé | 400 — 
- **POST** /v1/sms/otp/send — Envoyer un code OTP par SMS
  - Requis : phone, purpose
  - Réponse : 201 — OTP envoyé
- **POST** /v1/sms/otp/verify — Vérifier un code OTP
  - Requis : phone, code
  - Réponse : 200 — OTP valide | 400 — OTP invalide ou expiré
- **GET** /v1/sms/{id}/status — Statut de livraison d'un SMS
  - Requis : id
  - Réponse : 200 — Statut

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# soc-api

**Titre** : SOC API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Security Operations Center. Gestion des analystes, tickets et escalades.

## Endpoints
- **GET** /v1/soc/tickets — Tickets en cours
  - Réponse : 200 — OK
- **POST** /v1/soc/tickets — Créer ticket
  - Réponse : 200 — OK
- **GET** /v1/soc/tickets/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/soc/tickets/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/soc/tickets/{id} — Escalader
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/soc/analysts — Analystes disponibles
  - Réponse : 200 — OK
- **POST** /v1/soc/analysts — Assigner
  - Réponse : 200 — OK
- **GET** /v1/soc/metrics — KPIs SOC
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# soil-analysis-api

**Titre** : Soil Analysis API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Analyses de sol. pH, nutriments et recommandations fertilisation. DIFFERENCE vs field-api : Soil Analysis = analyses laboratoire ponctuelles, Field = gestion parcelle complète.

## Endpoints
- **GET** /v1/soil/analyses — Analyses en cours
  - Réponse : 200 — OK
- **POST** /v1/soil/analyses — Commander analyse
  - Réponse : 200 — OK
- **GET** /v1/soil/analyses/{id} — Recommandations fertilisation
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# solar-panel-api

**Titre** : Solar Panel API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Gestion panneaux solaires photovoltaïques. Production, rendement et maintenance.

## Endpoints
- **GET** /v1/solar-panels — Lister installations
  - Réponse : 200 — OK
- **POST** /v1/solar-panels — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/solar-panels/{id} — Production temps reel
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/solar-panels/{id}/performance — Rendement
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# spa-booking-api

**Titre** : Spa Booking API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Réservations spa et bien-être. Soins, thérapeutes et disponibilités.

## Endpoints
- **GET** /v1/spa/services — Services spa
  - Réponse : 200 — OK
- **GET** /v1/spa/bookings — Réservations
  - Réponse : 200 — OK
- **POST** /v1/spa/bookings — Réserver soin
  - Réponse : 200 — OK
- **GET** /v1/spa/bookings/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/spa/bookings/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# sso-api

**Titre** : SSO API
**Version** : v1 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Single Sign-On SAML 2.0 et OpenID Connect. Fédération d'identité avec les IdP externes (Azure AD, Okta, Google). DIFFÉRENCE vs auth-api : SSO = fédération vers IdP externes, Auth = authentification locale JWT.

## Endpoints
- **GET** /v1/sso/providers — Lister les IdP configurés
  - Réponse : 200 — Providers
- **POST** /v1/sso/providers — Configurer un IdP SSO
  - Requis : name, type, metadata_url
  - Réponse : 201 — IdP configuré
- **GET** /v1/sso/login/{providerId} — Initier le flux SSO (redirection vers IdP)
  - Requis : providerId
  - Réponse : 302 — Redirection vers l'IdP
- **POST** /v1/sso/callback — Callback SSO (assertion SAML ou code OIDC)
  - Réponse : 200 — JWT local généré

## Authentification
ApiKeyAuth — apiKey

---

# stock-reservation-api

**Titre** : Stock Reservation API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Réservation temporaire de stock lors du checkout. DIFFÉRENCE vs inventory-api : Stock Reservation = verrouillage temporaire (pendant la session panier), Inventory = stocks globaux et historique mouvements. Évite les surventes.

## Endpoints
- **POST** /v1/stock/reserve — Réserver du stock temporairement (TTL 15 min)
  - Réponse : 201 — Stock réservé | 409 — Stock insuffisant
- **GET** /v1/stock/reservations/{id} — Statut d'une réservation
  - Requis : id
  - Réponse : 200 — Réservation | 404 — 
- **DELETE** /v1/stock/reservations/{id} — Libérer la réservation
  - Requis : id
  - Réponse : 204 — Libérée
- **POST** /v1/stock/confirm/{reservationId} — Confirmer la réservation (stock déduit définitivement)
  - Requis : reservationId, order_id
  - Réponse : 200 — Confirmée — stock déduit

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# store-locator-api

**Titre** : Store Locator API
**Version** : v1 | **Statut** : active
**Domaine** : Localisation | **Équipe** : Equipe Commerce

## Description
Points de vente et magasins. Recherche par proximité, horaires et stocks en magasin.

## Endpoints
- **GET** /v1/stores/nearby — Magasins proches d'une position
  - Requis : lat, lng
  - Réponse : 200 — Magasins
- **GET** /v1/stores/{id} — Détails d'un magasin
  - Requis : id
  - Réponse : 200 — Magasin
- **GET** /v1/stores/{id}/hours — Horaires d'ouverture
  - Requis : id
  - Réponse : 200 — Horaires
- **GET** /v1/stores/{id}/stock/{productId} — Disponibilité d'un produit en magasin
  - Requis : id, productId
  - Réponse : 200 — Disponibilité

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# streaming-api

**Titre** : Streaming API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Traitement temps reel. Topics, consumers et offsets.

## Endpoints
- **GET** /v1/streaming/topics — Topics
  - Réponse : 200 — OK
- **POST** /v1/streaming/topics — Creer
  - Réponse : 200 — OK
- **DELETE** /v1/streaming/topics — Supprimer
  - Réponse : 200 — OK
- **POST** /v1/streaming/topics/{topic}/produce — Produire
  - Requis : topic
  - Réponse : 200 — OK
- **GET** /v1/streaming/topics/{topic}/consume — Consommer
  - Requis : topic
  - Réponse : 200 — OK
- **GET** /v1/streaming/consumers — Consumers
  - Réponse : 200 — OK
- **POST** /v1/streaming/consumers — Creer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# student-api-v1

**Titre** : Student API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Etudiants v1. DEPRECATED.

## Endpoints
- **GET** /v1/students — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# student-api-v2

**Titre** : Student API
**Version** : v2 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Gestion étudiants. Profils, inscriptions et parcours. DIFFERENCE vs employee-api : Student = apprenant (inscriptions, notes, parcours), Employee = salarié (RH, paie, contrat).

## Endpoints
- **GET** /v2/students — Lister étudiants
  - Réponse : 200 — OK
- **POST** /v2/students — Inscrire étudiant
  - Réponse : 200 — OK
- **GET** /v2/students/{id} — Profil étudiant
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/students/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/students/{id}/progress — Cours complétés
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/students/{id}/certificates — Certificats
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# subscriber-api-v1

**Titre** : Subscriber API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Abonnes v1. DEPRECATED.

## Endpoints
- **GET** /v1/subscribers — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# subscriber-api-v2

**Titre** : Subscriber API
**Version** : v2 | **Statut** : deprecated
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Abonnes v2 avec portabilite. DEPRECATED.

## Endpoints
- **GET** /v2/subscribers — Lister
  - Réponse : 200 — OK
- **POST** /v2/subscribers — Creer
  - Réponse : 200 — OK
- **POST** /v2/subscribers/{id}/portability — Porter numero
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# subscriber-api-v3

**Titre** : Subscriber API
**Version** : v3 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Gestion abonnes telecom. Lignes, forfaits, portabilite et cycle de vie. DIFFERENCE vs customer-profile-api : Subscriber = abonne telecom avec lignes/SIM, Customer Profile = client commercial generique.

## Endpoints
- **GET** /v3/subscribers — Abonnes
  - Réponse : 200 — OK
- **POST** /v3/subscribers — Creer
  - Réponse : 200 — OK
- **GET** /v3/subscribers/{id} — Profil
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/subscribers/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v3/subscribers/{id} — Resilier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/subscribers/{id}/lines — Lignes
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/subscribers/{id}/lines — Ajouter
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v3/subscribers/{id}/portability — Porter
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v3/subscribers/{id}/portability — Statut
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# subscription-api

**Titre** : Subscription API
**Version** : v2 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Abonnements produits et services. Plans, upgrades et résiliations. DIFFÉRENCE vs billing-api : Subscription = plan et droits d'accès, Billing = paiements récurrents.

## Endpoints
- **GET** /v2/subscriptions/{customerId} — Abonnements actifs d'un client
  - Requis : customerId
  - Réponse : 200 — Abonnements
- **POST** /v2/subscriptions — Souscrire à un plan
  - Requis : customer_id, plan_id
  - Réponse : 201 — Souscrit
- **PUT** /v2/subscriptions/{id}/upgrade — Upgrader vers un plan supérieur
  - Requis : id, new_plan_id
  - Réponse : 200 — Upgradé
- **PUT** /v2/subscriptions/{id}/downgrade — Downgrader vers un plan inférieur
  - Requis : id, new_plan_id
  - Réponse : 200 — Downgradé (effectif fin de période)
- **DELETE** /v2/subscriptions/{id} — Résilier l'abonnement
  - Requis : id
  - Réponse : 200 — Résilié

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# subsidy-api

**Titre** : Subsidy API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Aides et subventions agricoles. PAC, MSA et dossiers.

## Endpoints
- **GET** /v1/subsidies — Aides disponibles
  - Réponse : 200 — OK
- **GET** /v1/subsidies/{farmId} — Aides exploitation
  - Requis : farmId
  - Réponse : 200 — OK
- **POST** /v1/subsidies/{farmId} — Demander aide
  - Requis : farmId
  - Réponse : 200 — OK
- **GET** /v1/subsidies/applications/{id} — Statut dossier
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/subsidies/applications/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# supplier-api

**Titre** : Supplier API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Supply

## Description
Fournisseurs et partenaires B2B. Catalogue, contrats et évaluations.

## Endpoints
- **POST** /v1/suppliers — Créer un fournisseur
  - Requis : name, contact_email
  - Réponse : 201 — Créé
- **GET** /v1/suppliers — Lister les fournisseurs
  - Réponse : 200 — Fournisseurs
- **GET** /v1/suppliers/{id} — Fiche fournisseur
  - Requis : id
  - Réponse : 200 — Fournisseur
- **PUT** /v1/suppliers/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **GET** /v1/suppliers/{id}/products — Catalogue du fournisseur
  - Requis : id
  - Réponse : 200 — Produits
- **POST** /v1/suppliers/{id}/evaluate — Évaluer un fournisseur
  - Requis : id, score
  - Réponse : 201 — Évaluation enregistrée

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# supplier-quality-api

**Titre** : Supplier Quality API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Qualite fournisseurs. Evaluation, audits et non-conformites. DIFFERENCE vs quality-control-api : Supplier Quality = qualite entrants fournisseurs, Quality Control = qualite production interne.

## Endpoints
- **GET** /v1/supplier-quality/{supplierId} — Score qualite fournisseur
  - Requis : supplierId
  - Réponse : 200 — OK
- **GET** /v1/supplier-quality/audits — Audits fournisseurs
  - Réponse : 200 — OK
- **POST** /v1/supplier-quality/audits — Creer audit
  - Réponse : 200 — OK
- **GET** /v1/supplier-quality/ncs — NC fournisseurs
  - Réponse : 200 — OK
- **POST** /v1/supplier-quality/ncs — Declarer NC
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# surgery-scheduling-api

**Titre** : Surgery Scheduling API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Planification chirurgicale. Blocs opératoires, équipes chirurgicales et liste d'attente.

## Endpoints
- **GET** /v1/surgeries — Planning blocs
  - Réponse : 200 — OK
- **POST** /v1/surgeries — Planifier intervention
  - Réponse : 200 — OK
- **GET** /v1/surgeries/{id} — Détail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/surgeries/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/surgeries/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/or/availability — Disponibilité blocs
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# survey-api

**Titre** : Survey API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Enquêtes de satisfaction client. NPS, CSAT, création et analyse des résultats.

## Endpoints
- **POST** /v1/surveys — Créer une enquête
  - Requis : title, type
  - Réponse : 201 — Créée
- **POST** /v1/surveys/{id}/send — Envoyer l'enquête à des clients
  - Requis : id, customer_ids
  - Réponse : 202 — Envoyée
- **POST** /v1/surveys/{id}/respond — Soumettre une réponse
  - Requis : id, customer_id, answers
  - Réponse : 201 — Réponse enregistrée
- **GET** /v1/surveys/{id}/results — Résultats de l'enquête
  - Requis : id
  - Réponse : 200 — Résultats
- **GET** /v1/surveys/nps — Score NPS global
  - Réponse : 200 — NPS

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# synthetic-data-api

**Titre** : Synthetic Data API
**Version** : v1 | **Statut** : active
**Domaine** : Data | **Équipe** : Equipe Data

## Description
Generation donnees synthetiques. Modeles, seeds et validation.

## Endpoints
- **POST** /v1/synthetic/generate — Generer donnees synthetiques
  - Réponse : 200 — OK
- **GET** /v1/synthetic/models — Modeles
  - Réponse : 200 — OK
- **POST** /v1/synthetic/models — Entrainer modele
  - Réponse : 200 — OK
- **POST** /v1/synthetic/validate — Valider qualite
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tachograph-api

**Titre** : Tachograph API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Tachygraphe numérique. Temps de conduite, repos et conformité réglementaire.

## Endpoints
- **GET** /v1/tachograph/{driverId} — Données tachygraphe
  - Requis : driverId
  - Réponse : 200 — OK
- **POST** /v1/tachograph/{driverId} — Importer données
  - Requis : driverId
  - Réponse : 200 — OK
- **GET** /v1/tachograph/{driverId}/compliance — Infractions
  - Requis : driverId
  - Réponse : 200 — OK
- **GET** /v1/tachograph/{driverId}/rest-periods — Périodes de repos
  - Requis : driverId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tag-api

**Titre** : Tag API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Tags libres et labels sur les ressources (produits, tickets, contrats, clients). Taxonomie folksonomy. DIFFÉRENCE vs segmentation-api : Tag = étiquette libre assignée manuellement à une ressource spécifique, Segmentation = groupe dynamique calculé selon des règles comportementales sur des populations d'utilisateurs. DIFFÉRENCE vs product-catalog-api : Tag = label libre multi-domaine, Category = hiérarchie structurée propre au catalogue produit.

## Endpoints
- **GET** /v1/tags — Lister tous les tags disponibles
  - Réponse : 200 — Tags
- **POST** /v1/tags — Créer un tag
  - Requis : name
  - Réponse : 201 — Tag créé
- **PUT** /v1/tags/{id} — Mettre à jour un tag
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/tags/{id} — Supprimer un tag (dé-tagge toutes les ressources associées)
  - Requis : id
  - Réponse : 204 — Supprimé
- **POST** /v1/tags/assign — Assigner des tags à une ressource
  - Requis : resource_type, resource_id, tag_ids
  - Réponse : 200 — Tags assignés
- **GET** /v1/tags/resources — Ressources portant un ou plusieurs tags
  - Requis : tag_ids
  - Réponse : 200 — Ressources tagguées

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# task-api

**Titre** : Task API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Gestion des tâches et listes de tâches (todo). Assignation, priorités, dépendances et suivi d'avancement. DIFFÉRENCE vs ticket-api : Task = tâche de travail interne planifiée (projet, sprint, backlog), Ticket = demande entrante d'un client nécessitant une résolution (support). DIFFÉRENCE vs workflow-api : Task = unité de travail humain simple, Workflow = orchestration automatisée de processus multi-étapes.

## Endpoints
- **POST** /v1/tasks — Créer une tâche
  - Réponse : 201 — Tâche créée
- **GET** /v1/tasks — Lister les tâches
  - Réponse : 200 — Tâches
- **GET** /v1/tasks/{id} — Détails d'une tâche
  - Requis : id
  - Réponse : 200 — Tâche | 404 — 
- **PUT** /v1/tasks/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/tasks/{id} — Supprimer une tâche
  - Requis : id
  - Réponse : 204 — Supprimée
- **PATCH** /v1/tasks/{id}/status — Changer le statut rapidement
  - Requis : id, status
  - Réponse : 200 — Statut mis à jour
- **GET** /v1/tasks/{id}/dependencies — Dépendances d'une tâche (bloquantes/bloquées par)
  - Requis : id
  - Réponse : 200 — Dépendances
- **POST** /v1/tasks/{id}/dependencies — Ajouter une dépendance
  - Requis : id, task_id, type
  - Réponse : 201 — Dépendance ajoutée
- **GET** /v1/tasks/my — Tâches de l'utilisateur courant (mes tâches)
  - Réponse : 200 — Mes tâches

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# tax-api

**Titre** : Tax API
**Version** : v1 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Calcul des taxes et TVA selon les régions. Conformité fiscale internationale et déclarations.

## Endpoints
- **POST** /v1/tax/calculate — Calculer les taxes d'une transaction
  - Requis : amount, country
  - Réponse : 200 — Taxes calculées
- **GET** /v1/tax/rates — Taux de TVA par pays
  - Requis : country
  - Réponse : 200 — Taux
- **POST** /v1/tax/validate-vat — Valider un numéro de TVA intracommunautaire
  - Requis : vat_number
  - Réponse : 200 — Valide | 400 — Numéro invalide
- **GET** /v1/tax/reports — Rapport fiscal par période
  - Réponse : 200 — Rapport

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# team-api

**Titre** : Team API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Équipes de travail transverses et fonctionnelles. Création, membres et canaux de communication d'équipe. DIFFÉRENCE vs hr-api : Team API gère les équipes de travail fonctionnelles (equipe projet, squad produit), HR API gère les dossiers administratifs RH et la structure hiérarchique. DIFFÉRENCE vs account-api : Team = équipe interne de collaborateurs, Account = organisation cliente externe B2B. DIFFÉRENCE vs org-api : Team = équipe de travail opérationnelle, Org = entité juridique de l'entreprise.

## Endpoints
- **POST** /v1/teams — Créer une équipe
  - Réponse : 201 — Équipe créée
- **GET** /v1/teams — Lister les équipes
  - Réponse : 200 — Équipes
- **GET** /v1/teams/{id} — Équipe avec membres et KPIs
  - Requis : id
  - Réponse : 200 — Équipe | 404 — 
- **PUT** /v1/teams/{id} — Mettre à jour l'équipe
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/teams/{id} — Dissoudre une équipe
  - Requis : id
  - Réponse : 204 — Dissoute
- **GET** /v1/teams/{id}/members — Membres de l'équipe
  - Requis : id
  - Réponse : 200 — Membres
- **POST** /v1/teams/{id}/members — Ajouter un membre
  - Requis : id, user_id, role
  - Réponse : 201 — Membre ajouté
- **DELETE** /v1/teams/{id}/members/{userId} — Retirer un membre
  - Requis : id, userId
  - Réponse : 204 — Retiré
- **GET** /v1/teams/{id}/metrics — KPIs de l'équipe (vélocité, tâches complétées, OKRs)
  - Requis : id
  - Réponse : 200 — KPIs équipe

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# telemedicine-api

**Titre** : Telemedicine API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Téléconsultation médicale. Planification visio-consultations, salle d'attente virtuelle et compte-rendu.

## Endpoints
- **GET** /v1/teleconsult — Consultations planifiées
  - Réponse : 200 — OK
- **POST** /v1/teleconsult — Planifier
  - Réponse : 200 — OK
- **GET** /v1/teleconsult/{id} — Détail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/teleconsult/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/teleconsult/{id}/start — Démarrer session vidéo
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/teleconsult/{id}/summary — Ajouter compte-rendu
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# telemetry-api

**Titre** : Telemetry API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Données télémétrie équipements industriels. Agrégation, statistiques et anomalies. DIFFERENCE vs sensor-data-api : Telemetry = données agrégées équipements, Sensor Data = mesures brutes capteurs.

## Endpoints
- **GET** /v1/telemetry/{deviceId} — Données telemetrie
  - Requis : deviceId
  - Réponse : 200 — OK
- **POST** /v1/telemetry/{deviceId} — Envoyer telemetrie
  - Requis : deviceId
  - Réponse : 200 — OK
- **GET** /v1/telemetry/{deviceId}/stats — Statistiques
  - Requis : deviceId
  - Réponse : 200 — OK
- **GET** /v1/telemetry/{deviceId}/anomalies — Detecter anomalies
  - Requis : deviceId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tenant-api-v1

**Titre** : Tenant API
**Version** : v1 | **Statut** : deprecated
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Locataires v1. DEPRECATED.

## Endpoints
- **GET** /v1/tenants — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tenant-api-v2

**Titre** : Tenant API
**Version** : v2 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion locataires. Dossiers, scoring et suivi. DIFFERENCE vs customer-profile-api : Tenant = locataire immobilier (dossier location, garants), Customer Profile = client commercial générique.

## Endpoints
- **GET** /v2/tenants — Lister locataires
  - Réponse : 200 — OK
- **POST** /v2/tenants — Créer dossier
  - Réponse : 200 — OK
- **GET** /v2/tenants/{id} — Dossier locataire
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/tenants/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/tenants/{id}/scoring — Score solvabilite
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/tenants/{id}/guarantors — Garants
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/tenants/{id}/guarantors — Ajouter garant
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# threat-intelligence-api

**Titre** : Threat Intelligence API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Renseignement sur les menaces. IoC, acteurs malveillants et TTPs.

## Endpoints
- **GET** /v1/threats — Menaces actives
  - Réponse : 200 — OK
- **POST** /v1/threats — Ajouter menace
  - Réponse : 200 — OK
- **GET** /v1/threats/{id} — Detail menace
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/threats/ioc/check — Ingérer IoC
  - Réponse : 200 — OK
- **GET** /v1/threats/feeds — Flux renseignement
  - Réponse : 200 — OK
- **POST** /v1/threats/feeds — S'abonner
  - Réponse : 200 — OK
- **GET** /v1/threats/actors — Acteurs malveillants
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# ticket-api

**Titre** : Ticket API
**Version** : v1 | **Statut** : active
**Domaine** : Customer Support | **Équipe** : Equipe Support

## Description
Tickets de support client. Création, assignation, escalade et résolution des incidents.

## Endpoints
- **POST** /v1/tickets — Créer un ticket support
  - Requis : subject, description, customer_id
  - Réponse : 201 — Ticket créé
- **GET** /v1/tickets — Lister les tickets
  - Réponse : 200 — Tickets
- **GET** /v1/tickets/{id} — Détails d'un ticket
  - Requis : id
  - Réponse : 200 — Ticket
- **PUT** /v1/tickets/{id}/assign — Assigner à un agent
  - Requis : id, agent_id
  - Réponse : 200 — Assigné
- **PUT** /v1/tickets/{id}/escalate — Escalader un ticket
  - Requis : id, reason
  - Réponse : 200 — Escaladé
- **PUT** /v1/tickets/{id}/close — Fermer un ticket
  - Requis : id
  - Réponse : 200 — Fermé
- **POST** /v1/tickets/{id}/comments — Ajouter un commentaire au ticket
  - Requis : id, content
  - Réponse : 201 — Commentaire ajouté

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# time-tracking-api

**Titre** : Time Tracking API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Suivi du temps de travail. Pointage, heures supplémentaires et rapports d'activité.

## Endpoints
- **POST** /v1/time/clock-in — Pointer l'arrivée
  - Requis : employee_id
  - Réponse : 201 — Pointage enregistré
- **POST** /v1/time/clock-out — Pointer le départ
  - Requis : employee_id
  - Réponse : 200 — Départ enregistré
- **GET** /v1/time/{employeeId}/entries — Entrées de temps d'un employé
  - Requis : employeeId
  - Réponse : 200 — Entrées
- **GET** /v1/time/{employeeId}/summary — Résumé heures/semaine/mois
  - Requis : employeeId
  - Réponse : 200 — Résumé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# toll-api

**Titre** : Toll API
**Version** : v1 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion des péages et taxes de transit. Calcul coûts, télépéage et facturation.

## Endpoints
- **POST** /v1/tolls/calculate — Calculer péages itinéraire
  - Réponse : 200 — OK
- **GET** /v1/tolls/accounts/{vehicleId} — Compte télépéage
  - Requis : vehicleId
  - Réponse : 200 — OK
- **POST** /v1/tolls/accounts/{vehicleId} — Recharger compte
  - Requis : vehicleId
  - Réponse : 200 — OK
- **GET** /v1/tolls/transactions/{vehicleId} — Historique péages
  - Requis : vehicleId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tooling-api

**Titre** : Tooling API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Gestion outillage. Outils coupants, durees de vie et reconditionnement.

## Endpoints
- **GET** /v1/tooling — Outillage
  - Réponse : 200 — OK
- **POST** /v1/tooling — Ajouter outil
  - Réponse : 200 — OK
- **GET** /v1/tooling/{id} — Statut outil
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/tooling/{id} — Mettre a jour duree vie
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/tooling/{id}/reconditioning — Reconditionnements
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/tooling/{id}/reconditioning — Planifier
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# topology-api

**Titre** : Topology API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Topologie reseau. Carte, liens et capacite.

## Endpoints
- **GET** /v1/topology/map — Changements
  - Réponse : 200 — OK
- **GET** /v1/topology/links — Liens
  - Réponse : 200 — OK
- **POST** /v1/topology/links — Ajouter
  - Réponse : 200 — OK
- **GET** /v1/topology/links/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tour-operator-api

**Titre** : Tour Operator API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Gestion tours et excursions. Guides, groupes et itinéraires.

## Endpoints
- **GET** /v1/tours — Tours disponibles
  - Réponse : 200 — OK
- **POST** /v1/tours — Créer tour
  - Réponse : 200 — OK
- **GET** /v1/tours/{id} — Detail tour
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/tours/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/tours/{id}/bookings — Réservations
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/tours/{id}/bookings — Réserver place
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/tours/{id}/guides — Guides assignés
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/tours/{id}/guides — Assigner guide
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tower-management-api

**Titre** : Tower Management API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Antennes et pylones. Maintenance, partage et autorisations.

## Endpoints
- **GET** /v1/towers — Antennes
  - Réponse : 200 — OK
- **POST** /v1/towers — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/towers/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/towers/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/towers/{id}/maintenance — Maintenance
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/towers/{id}/maintenance — Planifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/towers/{id}/sharing — Accords partage
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# traceability-agri-api

**Titre** : Traceability Agri API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Traçabilité agricole de la ferme au consommateur. Certifications et labels. DIFFERENCE vs logistics-tracking-api : Traceability Agri = origine produit agricole (parcelle, traitement), Logistics = suivi colis transport.

## Endpoints
- **GET** /v1/traceability/{productId} — Parcours ferme-consommateur
  - Requis : productId
  - Réponse : 200 — OK
- **GET** /v1/traceability/{productId}/certificates — Certifications bio/HVE
  - Requis : productId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# traceability-industry-api

**Titre** : Traceability Industry API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Tracabilite produits industriels. Numeros serie, lots et historique. DIFFERENCE vs traceability-agri-api : Traceability Industry = tracabilite pieces et lots industriels, Traceability Agri = traçabilite produits agricoles.

## Endpoints
- **GET** /v1/traceability/{serialNumber} — Arbre composants
  - Requis : serialNumber
  - Réponse : 200 — OK
- **GET** /v1/traceability/lots/{lotId} — Expedition lot
  - Requis : lotId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# trading-api-v1

**Titre** : Trading API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Trading v1. DEPRECATED.

## Endpoints
- **POST** /v1/orders — Passer ordre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# trading-api-v2

**Titre** : Trading API
**Version** : v2 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Trading actions, obligations, derives. Ordres market/limit/stop. DIFFERENCE vs investment-api : Trading = execution temps reel marches, Investment = gestion epargne retail.

## Endpoints
- **GET** /v2/trading/orders — Carnet ordres
  - Réponse : 200 — OK
- **POST** /v2/trading/orders — Passer ordre
  - Réponse : 200 — OK
- **GET** /v2/trading/orders/{id} — Ordre
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/trading/orders/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/trading/market-data — Cotations temps reel
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# training-api

**Titre** : Training API
**Version** : v1 | **Statut** : active
**Domaine** : Human Resources | **Équipe** : Equipe RH

## Description
Formation professionnelle. Catalogue, inscriptions et suivi des compétences.

## Endpoints
- **GET** /v1/trainings — Catalogue des formations
  - Réponse : 200 — Formations
- **POST** /v1/trainings/{id}/enroll — S'inscrire à une formation
  - Requis : id, employee_id
  - Réponse : 201 — Inscrit
- **GET** /v1/trainings/{employeeId}/completed — Formations complétées par un employé
  - Requis : employeeId
  - Réponse : 200 — Formations
- **GET** /v1/skills/{employeeId} — Compétences validées d'un employé
  - Requis : employeeId
  - Réponse : 200 — Compétences
- **PUT** /v1/skills/{employeeId} — Mettre à jour les compétences
  - Requis : employeeId

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# transfer-api-v1

**Titre** : Transfer API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Virements v1. DEPRECATED.

## Endpoints
- **POST** /v1/transfers — Virer
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# transfer-api-v2

**Titre** : Transfer API
**Version** : v2 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Virements SEPA, SWIFT et instantane. DIFFERENCE vs payout-api : Transfer = virement entre comptes bancaires, Payout = reversement plateforme vers vendeur.

## Endpoints
- **GET** /v2/transfers — Historique
  - Réponse : 200 — OK
- **POST** /v2/transfers — Creer virement
  - Réponse : 200 — OK
- **GET** /v2/transfers/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v2/transfers/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/transfers/validate-iban — Valider IBAN
  - Réponse : 200 — OK
- **POST** /v2/transfers/fees — Calculer frais
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# translation-api

**Titre** : Translation API
**Version** : v1 | **Statut** : active
**Domaine** : Localisation | **Équipe** : Equipe Platform

## Description
Traduction automatique de contenu. API de traduction NMT (Neural Machine Translation) pour textes et documents. DIFFÉRENCE vs localization-api : Translation API = traduction de texte brut via NMT, Localization API = gestion des clés de traduction i18n et des formats culturels.

## Endpoints
- **POST** /v1/translate — Traduire un texte
  - Requis : text, target_language
  - Réponse : 200 — Texte traduit avec langue détectée
- **POST** /v1/translate/batch — Traduire plusieurs textes en une requête
  - Requis : texts, target_language
  - Réponse : 200 — Traductions
- **GET** /v1/translate/languages — Langues supportées
  - Réponse : 200 — Langues
- **POST** /v1/translate/detect — Détecter la langue d'un texte
  - Requis : text
  - Réponse : 200 — Langue détectée avec confiance

## Authentification
ApiKeyAuth — apiKey

---

# travel-insurance-api

**Titre** : Travel Insurance API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Assurance voyage. Annulation, rapatriement et bagages. DIFFERENCE vs life-insurance-api : Travel Insurance = assurance ponctuelle voyage, Life Insurance = assurance vie long terme.

## Endpoints
- **POST** /v1/travel-insurance/quote — Obtenir devis
  - Réponse : 200 — OK
- **GET** /v1/travel-insurance/policies — Contrats voyage
  - Réponse : 200 — OK
- **POST** /v1/travel-insurance/policies — Souscrire
  - Réponse : 200 — OK
- **GET** /v1/travel-insurance/claims — Sinistres voyage
  - Réponse : 200 — OK
- **POST** /v1/travel-insurance/claims — Déclarer sinistre
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# travel-package-api

**Titre** : Travel Package API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Forfaits voyage. Séjours tout inclus, circuits et personnalisation.

## Endpoints
- **GET** /v1/packages — Forfaits disponibles
  - Réponse : 200 — OK
- **POST** /v1/packages — Créer forfait
  - Réponse : 200 — OK
- **GET** /v1/packages/{id} — Detail forfait
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/packages/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/packages/{id}/book — Réserver forfait
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/packages/{id}/book — Disponibilité
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# trip-api-v1

**Titre** : Trip API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Trajets v1. DEPRECATED.

## Endpoints
- **GET** /v1/trips — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# trip-api-v2

**Titre** : Trip API
**Version** : v2 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Gestion trajets et missions. Planification, suivi temps réel et bilan. DIFFERENCE vs route-optimization-api : Trip = trajet effectué, Route = calcul optimal d'itinéraire.

## Endpoints
- **GET** /v2/trips — Lister trajets
  - Réponse : 200 — OK
- **POST** /v2/trips — Créer trajet
  - Réponse : 200 — OK
- **GET** /v2/trips/{id} — Detail trajet
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/trips/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/trips/{id} — Terminer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/trips/{id}/waypoints — Points de passage
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/trips/{id}/waypoints — Ajouter point
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# tutor-api

**Titre** : Tutor API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Tutorat et accompagnement. Mise en relation tuteurs/étudiants et sessions.

## Endpoints
- **GET** /v1/tutors — Tuteurs disponibles
  - Réponse : 200 — OK
- **POST** /v1/tutors — S'inscrire comme tuteur
  - Réponse : 200 — OK
- **GET** /v1/tutors/{id} — Disponibilités
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/tutoring/sessions — Sessions
  - Réponse : 200 — OK
- **POST** /v1/tutoring/sessions — Réserver session
  - Réponse : 200 — OK
- **GET** /v1/tutoring/sessions/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/tutoring/sessions/{id} — Annuler
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# underwriting-api

**Titre** : Underwriting API
**Version** : v1 | **Statut** : active
**Domaine** : Insurance | **Équipe** : Equipe Assurance

## Description
Souscription et acceptation du risque. Évaluation, décision et conditions.

## Endpoints
- **POST** /v1/underwriting/evaluate — Évaluer risque
  - Réponse : 200 — OK
- **GET** /v1/underwriting/{applicationId} — Décision souscription
  - Requis : applicationId
  - Réponse : 200 — OK
- **PUT** /v1/underwriting/{applicationId} — Modifier decision
  - Requis : applicationId
  - Réponse : 200 — OK
- **GET** /v1/underwriting/rules — Règles acceptation
  - Réponse : 200 — OK
- **POST** /v1/underwriting/rules — Ajouter règle
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# user-api-v1

**Titre** : User API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Version 1 de l'API utilisateurs. DEPRECATED 2022. Pas de 2FA, rôles simples (admin/user), pas de statut suspendu. Migrer vers v2.

## Endpoints
- **POST** /v1/users — Créer un utilisateur (sans 2FA)
  - Réponse : 201 — Créé | 409 — 
- **GET** /v1/users — Lister les utilisateurs
  - Réponse : 200 — Liste
- **GET** /v1/users/{id} — Profil utilisateur
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/users/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/users/{id} — Supprimer définitivement (BREAKING v2: soft delete)
  - Requis : id
  - Réponse : 204 — Supprimé

## Authentification
ApiKeyAuth — Clé API Kong Gateway — contacter votre équipe platform

---

# user-api-v3

**Titre** : User API
**Version** : v3 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Version actuelle recommandée. Ajout de la gestion des identités fédérées (SSO externe), des groupes d'utilisateurs, du provisioning SCIM 2.0 et de l'audit trail complet. DIFFÉRENCE vs user-api-v2 : v3 introduit SCIM, les groupes natifs et la délégation de rôles.

## Endpoints
- **POST** /v3/users — Créer utilisateur avec groupes et IdP liés
  - Réponse : 201 — Créé | 409 — 
- **GET** /v3/users — Lister avec filtres SCIM-compatibles
  - Réponse : 200 — Liste
- **GET** /v3/users/{id} — Profil complet avec groupes et IdP
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v3/users/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v3/users/{id} — Désactiver (soft delete avec audit)
  - Requis : id
  - Réponse : 204 — Désactivé
- **GET** /v3/users/{id}/groups — Groupes d'un utilisateur
  - Requis : id
  - Réponse : 200 — Groupes
- **POST** /v3/users/{id}/groups — Ajouter à un groupe
  - Requis : id, group_id
  - Réponse : 200 — Ajouté
- **GET** /v3/groups — Lister les groupes
  - Réponse : 200 — Groupes
- **POST** /v3/groups — Créer un groupe
  - Requis : name
  - Réponse : 201 — Créé
- **GET** /v3/scim/v2/Users — Endpoint SCIM 2.0 — liste des utilisateurs (nouveau en v3)
  - Réponse : 200 — SCIM UserList
- **POST** /v3/scim/v2/Users — Endpoint SCIM 2.0 — provisionner un utilisateur
  - Réponse : 201 — Provisionné

## Authentification
ApiKeyAuth — Clé API Kong Gateway — Devoteam nexDigital

---

# user-api

**Titre** : User API
**Version** : v2 | **Statut** : active
**Domaine** : Identity & Access | **Équipe** : Equipe Identity

## Description
Gestion des comptes utilisateurs : credentials, 2FA, préférences de compte. Couvre clients, employés, partenaires et admins. DIFFÉRENCE vs customer-profile-api : User = identité technique (login/mdp/2FA). Customer Profile = données commerciales (segmentation, achats). DIFFÉRENCE vs employee-api : User ne contient pas les données RH. DIFFÉRENCE vs account-api : User est une personne physique, Account est une organisation.

## Endpoints
- **POST** /v2/users — Créer un compte utilisateur
  - Réponse : 201 — Créé | 409 — 
- **GET** /v2/users/{id} — Récupérer un utilisateur
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v2/users/{id} — Mettre à jour
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v2/users/{id} — Désactiver un compte
  - Requis : id
  - Réponse : 204 — Désactivé
- **PUT** /v2/users/{id}/password — Changer le mot de passe
  - Requis : id, current_password, new_password
  - Réponse : 200 — Changé
- **POST** /v2/users/{id}/2fa — Activer le 2FA
  - Requis : id
  - Réponse : 200 — QR Code généré
- **DELETE** /v2/users/{id}/2fa — Désactiver le 2FA
  - Requis : id
  - Réponse : 200 — Désactivé

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# utility-management-api

**Titre** : Utility Management API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion fluides et services. Eau, électricité, gaz et internet dans les logements.

## Endpoints
- **GET** /v1/utilities/{propertyId} — Services actifs
  - Requis : propertyId
  - Réponse : 200 — OK
- **POST** /v1/utilities/{propertyId} — Activer service
  - Requis : propertyId
  - Réponse : 200 — OK
- **GET** /v1/utilities/{propertyId}/readings — Relevés
  - Requis : propertyId
  - Réponse : 200 — OK
- **POST** /v1/utilities/{propertyId}/readings — Soumettre relevé
  - Requis : propertyId
  - Réponse : 200 — OK
- **GET** /v1/utilities/{propertyId}/invoices — Factures
  - Requis : propertyId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vaccination-api

**Titre** : Vaccination API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Carnet de vaccination électronique. Historique vaccins, rappels et conformité aux schémas vaccinaux.

## Endpoints
- **GET** /v1/vaccinations/{patientId} — Carnet vaccinal
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/vaccinations/{patientId} — Enregistrer vaccin
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/vaccinations/{patientId}/due — Vaccins à faire
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/vaccinations/campaigns — Campagnes vaccinales
  - Réponse : 200 — OK
- **POST** /v1/vaccinations/campaigns — Créer campagne
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vehicle-api-v1

**Titre** : Vehicle API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Données véhicule v1. DEPRECATED.

## Endpoints
- **GET** /v1/vehicles/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vehicle-api-v2

**Titre** : Vehicle API
**Version** : v2 | **Statut** : active
**Domaine** : Transport | **Équipe** : Equipe Transport

## Description
Données techniques véhicule. Diagnostics OBD, kilométrage et état. DIFFERENCE vs fleet-api : Vehicle = données techniques d'un seul véhicule, Fleet = gestion de l'ensemble de la flotte.

## Endpoints
- **GET** /v2/vehicles/{id} — Données véhicule
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/vehicles/{id} — Modifier
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/vehicles/{id}/diagnostics — Diagnostics OBD
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/vehicles/{id}/diagnostics — Lancer diagnostic
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/vehicles/{id}/mileage — Kilométrage
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# veterinary-api

**Titre** : Veterinary API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Services veterinaires elevage. Visites, vaccinations et prescriptions. DIFFERENCE vs allergy-api : Veterinary = soins animaux d'elevage, Allergy = allergies patients humains.

## Endpoints
- **GET** /v1/veterinary/{animalId} — Historique veterinaire
  - Requis : animalId
  - Réponse : 200 — OK
- **POST** /v1/veterinary/{animalId} — Ajouter visite
  - Requis : animalId
  - Réponse : 200 — OK
- **GET** /v1/veterinary/{animalId}/treatments — Traitements
  - Requis : animalId
  - Réponse : 200 — OK
- **POST** /v1/veterinary/{animalId}/treatments — Prescrire
  - Requis : animalId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# virtual-classroom-api

**Titre** : Virtual Classroom API
**Version** : v1 | **Statut** : active
**Domaine** : Education | **Équipe** : Equipe Education

## Description
Classes virtuelles. Salles de cours en ligne, partage écran et enregistrement.

## Endpoints
- **GET** /v1/classrooms — Classes planifiées
  - Réponse : 200 — OK
- **POST** /v1/classrooms — Créer classe
  - Réponse : 200 — OK
- **GET** /v1/classrooms/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/classrooms/{id} — Démarrer cours
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/classrooms/{id} — Terminer cours
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/classrooms/{id}/participants — Participants
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/classrooms/{id}/participants — Inviter
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/classrooms/{id}/recording — Enregistrement
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# visa-api

**Titre** : Visa API
**Version** : v1 | **Statut** : active
**Domaine** : Tourism | **Équipe** : Equipe Tourisme

## Description
Formalités visa et entrée pays. Vérification exigences et suivi demande.

## Endpoints
- **POST** /v1/visa/requirements — Vérifier exigences visa
  - Réponse : 200 — OK
- **GET** /v1/visa/applications — Demandes
  - Réponse : 200 — OK
- **POST** /v1/visa/applications — Soumettre demande
  - Réponse : 200 — OK
- **GET** /v1/visa/applications/{id} — Statut demande
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v1/visa/applications/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# visitor-management-api

**Titre** : Visitor Management API
**Version** : v1 | **Statut** : active
**Domaine** : RealEstate | **Équipe** : Equipe Immobilier

## Description
Gestion visiteurs et accès immeubles. Badges, invitations et journal des accès.

## Endpoints
- **GET** /v1/visitors — Visiteurs du jour
  - Réponse : 200 — OK
- **POST** /v1/visitors — Pré-enregistrer
  - Réponse : 200 — OK
- **GET** /v1/visitors/{id} — Detail
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/visitors/{id} — Enregistrer sortie
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/visitors/access-log — Journal des accès
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vital-signs-api

**Titre** : Vital Signs API
**Version** : v1 | **Statut** : active
**Domaine** : Healthcare | **Équipe** : Equipe Santé

## Description
Constantes physiologiques temps réel : tension, pouls, température, SpO2. DIFFÉRENCE vs lab-result-api : Vital Signs = mesures continues IoT médical, Lab = analyses biologiques ponctuelles.

## Endpoints
- **GET** /v1/vitals/{patientId} — Constantes récentes
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/vitals/{patientId} — Enregistrer mesure
  - Requis : patientId
  - Réponse : 200 — OK
- **GET** /v1/vitals/{patientId}/alerts — Alertes seuils
  - Requis : patientId
  - Réponse : 200 — OK
- **POST** /v1/vitals/{patientId}/alerts — Configurer seuil
  - Requis : patientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# voip-api

**Titre** : VoIP API
**Version** : v1 | **Statut** : active
**Domaine** : Telecom | **Équipe** : Equipe Telecom

## Description
Telephonie sur IP. Appels, conferences et enregistrements.

## Endpoints
- **GET** /v1/voip/calls — Historique
  - Réponse : 200 — OK
- **POST** /v1/voip/calls — Initier appel
  - Réponse : 200 — OK
- **GET** /v1/voip/calls/{id} — Statut
  - Requis : id
  - Réponse : 200 — OK
- **DELETE** /v1/voip/calls/{id} — Raccrocher
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/voip/conferences — Conferences
  - Réponse : 200 — OK
- **POST** /v1/voip/conferences — Creer
  - Réponse : 200 — OK
- **GET** /v1/voip/conferences/{id}/participants — Participants
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/voip/conferences/{id}/participants — Ajouter
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vulnerability-api-v1

**Titre** : Vulnerability API
**Version** : v1 | **Statut** : deprecated
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Vulnérabilités v1. DEPRECATED.

## Endpoints
- **GET** /v1/vulnerabilities — Lister
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vulnerability-api-v2

**Titre** : Vulnerability API
**Version** : v2 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Gestion vulnérabilités. CVE, CVSS scoring et remediation. DIFFERENCE vs security-incident-api : Vulnerability = faille connue non exploitée, Security Incident = incident en cours actif.

## Endpoints
- **GET** /v2/vulnerabilities — Vulnérabilités détectées
  - Réponse : 200 — OK
- **POST** /v2/vulnerabilities — Signaler
  - Réponse : 200 — OK
- **GET** /v2/vulnerabilities/{id} — Detail CVE
  - Requis : id
  - Réponse : 200 — OK
- **PUT** /v2/vulnerabilities/{id} — Statut remediation
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v2/vulnerabilities/{id}/patch — Info patch
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/vulnerabilities/{id}/patch — Appliquer patch
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v2/vulnerabilities/scan — Lancer scan
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# vulnerability-scanner-api

**Titre** : Vulnerability Scanner API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Scanner vulnerabilites automatise. Scans planifies et rapports. DIFFERENCE vs vulnerability-api-v2 : Scanner = detection automatique, Vulnerability = gestion cycle de vie failles.

## Endpoints
- **GET** /v1/scanner/scans — Scans
  - Réponse : 200 — OK
- **POST** /v1/scanner/scans — Creer scan
  - Réponse : 200 — OK
- **GET** /v1/scanner/scans/{id} — Rapport
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/scanner/scans/{id} — Lancer
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/scanner/targets — Cibles
  - Réponse : 200 — OK
- **POST** /v1/scanner/targets — Ajouter cible
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# wallet-api

**Titre** : Wallet API
**Version** : v1 | **Statut** : active
**Domaine** : Finance | **Équipe** : Equipe Finance

## Description
Portefeuille électronique interne. Crédits, rechargements et utilisation du solde plateforme. DIFFÉRENCE vs payment-api : Wallet = solde interne plateforme, Payment = transactions externes (carte/bank). Cas d'usage : crédits de remboursement, cashback, avoir en solde.

## Endpoints
- **GET** /v1/wallets/{userId} — Solde du portefeuille
  - Requis : userId
  - Réponse : 200 — Solde
- **POST** /v1/wallets/{userId}/topup — Recharger le portefeuille
  - Requis : userId, amount, currency
  - Réponse : 200 — Rechargé
- **POST** /v1/wallets/{userId}/debit — Débiter le portefeuille
  - Requis : userId, amount, order_id
  - Réponse : 200 — Débité | 400 — Solde insuffisant
- **GET** /v1/wallets/{userId}/transactions — Historique des transactions du portefeuille
  - Requis : userId
  - Réponse : 200 — Transactions

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# warehouse-api

**Titre** : Warehouse API
**Version** : v1 | **Statut** : active
**Domaine** : Supply Chain | **Équipe** : Equipe Logistique

## Description
Entrepôts et emplacements physiques. Mouvements de stock inter-entrepôts. DIFFÉRENCE vs inventory-api : Warehouse = où sont les produits (entrepôt, allée, étagère), Inventory = combien en stock.

## Endpoints
- **GET** /v1/warehouses — Lister les entrepôts
  - Réponse : 200 — Entrepôts
- **GET** /v1/warehouses/{id}/stock — Stock d'un entrepôt
  - Requis : id
  - Réponse : 200 — Stock
- **POST** /v1/warehouses/transfer — Transférer du stock entre entrepôts
  - Requis : product_id, from_warehouse, to_warehouse, quantity
  - Réponse : 202 — Transfert initié
- **GET** /v1/warehouses/{id}/locations — Emplacements dans un entrepôt (allées, étagères)
  - Requis : id
  - Réponse : 200 — Emplacements

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# waste-management-api

**Titre** : Waste-Management API
**Version** : v1 | **Statut** : active
**Domaine** : Industry | **Équipe** : Equipe Industrie

## Description
Gestion dechets industriels. Tri, traceabilite et reporting reglementaire.

## Endpoints
- **GET** /v1/waste/streams — Flux dechets
  - Réponse : 200 — OK
- **POST** /v1/waste/streams — Ajouter flux
  - Réponse : 200 — OK
- **GET** /v1/waste/records — Enregistrements
  - Réponse : 200 — OK
- **POST** /v1/waste/records — Declarer dechet
  - Réponse : 200 — OK
- **GET** /v1/waste/reports — Rapport dechets
  - Réponse : 200 — OK
- **POST** /v1/waste/reports — Rapport reglementaire
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# water-meter-api

**Titre** : Water Meter API
**Version** : v1 | **Statut** : active
**Domaine** : IoT | **Équipe** : Equipe IoT

## Description
Compteurs eau intelligents. Consommation, fuites et facturation. DIFFERENCE vs smart-meter-api : Water Meter = eau uniquement avec detection fuites, Smart Meter = multi-fluides generique.

## Endpoints
- **GET** /v1/water-meters — Lister
  - Réponse : 200 — OK
- **POST** /v1/water-meters — Enregistrer
  - Réponse : 200 — OK
- **GET** /v1/water-meters/{id} — Releve eau
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/water-meters/{id}/leak-detection — Detecter fuites
  - Requis : id
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# water-quality-api

**Titre** : Water Quality API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Qualite eau irrigation. Analyses, parametres et conformite. DIFFERENCE vs air-quality-api : Water Quality = eau usage agricole, Air Quality = qualite air.

## Endpoints
- **GET** /v1/water-quality/{sourceId} — Parametres eau
  - Requis : sourceId
  - Réponse : 200 — OK
- **POST** /v1/water-quality/{sourceId} — Ajouter analyse
  - Requis : sourceId
  - Réponse : 200 — OK
- **GET** /v1/water-quality/{sourceId}/compliance — Conformite
  - Requis : sourceId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# wealth-api

**Titre** : Wealth API
**Version** : v1 | **Statut** : active
**Domaine** : Banking | **Équipe** : Equipe Banque

## Description
Gestion de patrimoine. Bilan patrimonial, optimisation fiscale et succession clients premium.

## Endpoints
- **GET** /v1/wealth/{clientId} — Bilan patrimonial
  - Requis : clientId
  - Réponse : 200 — OK
- **PUT** /v1/wealth/{clientId} — Objectifs
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/wealth/{clientId}/tax-optimization — Recommandations fiscales
  - Requis : clientId
  - Réponse : 200 — OK
- **GET** /v1/wealth/{clientId}/estate-plan — Plan succession
  - Requis : clientId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# weather-forecast-agri-api

**Titre** : Weather Forecast Agri API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Météo agricole hyperlocale. Prévisions, gelées et risques. DIFFERENCE vs energy-forecast-api : Weather Forecast Agri = météo parcelle agricole, Energy Forecast = prévisions consommation énergie.

## Endpoints
- **GET** /v1/weather/{fieldId} — Prévisions 10j
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v1/weather/{fieldId}/frost-alerts — Alertes gelée
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v1/weather/{fieldId}/agro-indices — Indices agrométéo
  - Requis : fieldId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# webhook-api

**Titre** : Webhook API
**Version** : v1 | **Statut** : active
**Domaine** : Communication | **Équipe** : Equipe Platform

## Description
Enregistrement et gestion des webhooks entrants/sortants. Réception d'événements externes et diffusion d'événements internes vers des endpoints configurés. Validation des signatures HMAC.

## Endpoints
- **POST** /v1/webhooks — Enregistrer un endpoint webhook
  - Réponse : 201 — Enregistré
- **GET** /v1/webhooks — Lister les webhooks
  - Réponse : 200 — Liste
- **GET** /v1/webhooks/{id} — Détails d'un webhook
  - Requis : id
  - Réponse : 200 — OK | 404 — 
- **PUT** /v1/webhooks/{id} — Mettre à jour un webhook
  - Requis : id
  - Réponse : 200 — Mis à jour
- **DELETE** /v1/webhooks/{id} — Supprimer un webhook
  - Requis : id
  - Réponse : 204 — Supprimé
- **POST** /v1/webhooks/{id}/test — Envoyer un événement de test
  - Requis : id
  - Réponse : 200 — Test envoyé | 502 — Endpoint inaccessible
- **GET** /v1/webhooks/{id}/deliveries — Historique des livraisons
  - Requis : id
  - Réponse : 200 — Livraisons

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# whistleblowing-api

**Titre** : Whistleblowing API
**Version** : v1 | **Statut** : active
**Domaine** : Legal | **Équipe** : Equipe Legal

## Description
Signalement alerte ethique. Canal securise, anonymat et suivi. Loi Sapin II.

## Endpoints
- **POST** /v1/whistleblowing/alerts — Signaler anonymement
  - Réponse : 200 — OK
- **GET** /v1/whistleblowing/alerts — Signalements recus
  - Réponse : 200 — OK
- **GET** /v1/whistleblowing/alerts/{id} — Statut signalement
  - Requis : id
  - Réponse : 200 — OK
- **POST** /v1/whistleblowing/alerts/{id} — Mettre a jour
  - Requis : id
  - Réponse : 200 — OK
- **GET** /v1/whistleblowing/config — Config canal
  - Réponse : 200 — OK
- **PUT** /v1/whistleblowing/config — Modifier
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# wishlist-api

**Titre** : Wishlist API
**Version** : v1 | **Statut** : active
**Domaine** : E-Commerce | **Équipe** : Equipe Commerce

## Description
Listes de souhaits clients. Produits désirés sans intention d'achat immédiate, partage et notifications de disponibilité. DIFFÉRENCE vs cart-api : Wishlist = désirs futurs, Cart = intention d'achat immédiate.

## Endpoints
- **GET** /v1/wishlists/{userId} — Récupérer la wishlist
  - Requis : userId
  - Réponse : 200 — Wishlist
- **POST** /v1/wishlists/{userId}/items — Ajouter un produit
  - Requis : userId, product_id
  - Réponse : 201 — Ajouté
- **DELETE** /v1/wishlists/{userId}/items/{itemId} — Supprimer de la wishlist
  - Requis : userId, itemId
  - Réponse : 204 — Supprimé
- **POST** /v1/wishlists/{userId}/share — Partager la wishlist
  - Requis : userId
  - Réponse : 200 — Partagée
- **POST** /v1/wishlists/{userId}/move-to-cart — Déplacer des articles vers le panier
  - Requis : userId
  - Réponse : 200 — Déplacé vers panier

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# workflow-api

**Titre** : Workflow API
**Version** : v1 | **Statut** : active
**Domaine** : Operations | **Équipe** : Equipe Platform

## Description
Orchestration de workflows métier. Définition, exécution et suivi des processus automatisés.

## Endpoints
- **POST** /v1/workflows — Créer un workflow
  - Requis : name, steps
  - Réponse : 201 — Créé
- **GET** /v1/workflows — Lister les workflows
  - Réponse : 200 — Workflows
- **POST** /v1/workflows/{id}/start — Démarrer une instance du workflow
  - Requis : id
  - Réponse : 201 — Instance démarrée
- **GET** /v1/workflows/{id}/status — Statut d'une instance
  - Requis : id
  - Réponse : 200 — Statut
- **PUT** /v1/workflows/{id}/cancel — Annuler une instance en cours
  - Requis : id
  - Réponse : 200 — Annulé
- **GET** /v1/workflows/{id}/history — Historique des exécutions
  - Requis : id
  - Réponse : 200 — Historique

## Authentification
ApiKeyAuth — Clé API Kong Gateway

---

# yield-prediction-api

**Titre** : Yield Prediction API
**Version** : v1 | **Statut** : active
**Domaine** : Agriculture | **Équipe** : Equipe Agriculture

## Description
Prévisions rendements par IA. Modèles satellites et météo. DIFFERENCE vs crop-api : Yield Prediction = modèle prédictif ML, Crop = données réelles cultures.

## Endpoints
- **GET** /v1/yield/{fieldId} — Prédiction rendement
  - Requis : fieldId
  - Réponse : 200 — OK
- **POST** /v1/yield/{fieldId} — Lancer modèle
  - Requis : fieldId
  - Réponse : 200 — OK
- **GET** /v1/yield/{fieldId}/scenarios — Scénarios prédiction
  - Requis : fieldId
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---

# zero-trust-api

**Titre** : Zero Trust API
**Version** : v1 | **Statut** : active
**Domaine** : Cybersecurity | **Équipe** : Equipe Cybersécurité

## Description
Architecture Zero Trust. Vérification continue identité et accès contextuels.

## Endpoints
- **POST** /v1/zerotrust/verify — Vérifier accès Zero Trust
  - Réponse : 200 — OK
- **GET** /v1/zerotrust/policies — Politiques ZTA
  - Réponse : 200 — OK
- **POST** /v1/zerotrust/policies — Créer politique
  - Réponse : 200 — OK
- **GET** /v1/zerotrust/sessions — Sessions actives
  - Réponse : 200 — OK
- **DELETE** /v1/zerotrust/sessions — Révoquer session
  - Réponse : 200 — OK

## Authentification
ApiKeyAuth — apiKey

---
