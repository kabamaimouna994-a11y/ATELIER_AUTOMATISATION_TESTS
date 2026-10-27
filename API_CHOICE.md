# API Choice

- Étudiante : Maïmouna Kaba
- API choisie : Quotable
- URL base : https://api.quotable.io/random
- Documentation officielle / README : https://github.com/lukePeavey/quotable
- Auth : None
- Endpoints testés :
  - GET /random
- Hypothèses de contrat (champs attendus, types, codes) :
  - Code HTTP : 200 OK
  - Content-Type : application/json
  - Champs obligatoires : `content` (string), `author` (string)
- Limites / rate limiting connu : Utilisation libre et généreuse (pas de clé requise).
- Risques : Très stable, aucun risque majeur.
