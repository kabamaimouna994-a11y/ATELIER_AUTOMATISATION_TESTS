# API Choice

- Étudiante : Maïmouna Kaba
- API choisie : Agify
- URL base : https://api.agify.io
- Documentation officielle / README : https://agify.io
- Auth : None
- Endpoints testés :
  - GET /?name=maimouna
- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP : 200 OK
  - Content-Type : application/json
  - Champs obligatoires : `name` (string), `age` (int ou null), `count` (int)
- Limites / rate limiting connu : Gratuit jusqu'à 1000 requêtes par jour.
- Risques : Service très stable, aucun risque majeur.
