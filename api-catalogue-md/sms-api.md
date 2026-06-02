# SMS API (sms-api)
Version v1 - statut : active
Domaine : Communication
Equipe : Equipe Platform

Envoi de SMS transactionnels et OTP. Canal SMS seul. DIFFÉRENCE vs notification-api : SMS API = canal SMS avec numéros courts dédiés, Notification API = façade multi-canal. DIFFÉRENCE vs messaging-api : SMS = externe vers mobile, Messaging = chat in-app bidirectionnel.

## Endpoints
- POST /v1/sms/send : Envoyer un SMS transactionnel
- POST /v1/sms/otp/send : Envoyer un code OTP par SMS
- POST /v1/sms/otp/verify : Vérifier un code OTP
- GET /v1/sms/{id}/status : Statut de livraison d'un SMS

Authentification : Clé API Kong Gateway