## Résumé

Site web d'Orange County Lettings

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Cloner le repository

- `cd /path/to/put/project/in`
- `git clone https://github.com/OpenClassrooms-Student-Center/Python-OC-Lettings-FR.git`

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`

###Perso:
enlever heroku config:set DISABLE_COLLECTSTATIC=1 si besoin de mettre des statics
il faut create avant le déploiement sur heroku juste une fois
variables:
DOCKER_LOGIN
DOCKER_PASSWORD
HEROKU_API_KEY
HEROKU_APP_NAME
la secret_key est nécessaire pour le déploiement 
(sans celle-ci le pipeline passerait mais pas lorsque l'on irait sur le site)
SECRET_KEY

Procfile: https://devcenter.heroku.com/articles/release-phase

pour avoir HEROKU_API_KEY:
soit `heroku authorizations:create` pour la production 
soit `heroku auth:token` pour le développement

pour la secret key:
on pourra donner une valeur via une variable sur circleci faisant lien avec
`heroku config:set SECRET_KEY=$SECRET_KEY`

pour voir si tout est bon pour le deploiement : 
`heroku run python manage.py check --deploy -a oc-lettings-lp`

Pour sentry, 
il faut lancer le projet avec `python3 manage.py runserver`
ensuite après avoir créer un compte sur Sentry, aller dans Projects puis Create Projects
à ce moment là on peut récupérer le DSN affiché et le mettre dans nos variablesil faut un DSN qui est trouvable après s'être inscrit en allant dans settings --> project --> client keys