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

### CircleCI & Déploiement:
Pour commencer s'inscrire sur CircleCI, Docker et Heroku :   
- CircleCI: `https://circleci.com/signup/`
- Docker: `https://hub.docker.com/signup`
- Heroku: `https://signup.heroku.com`   

Ensuite, après avoir mis le projet sur votre compte GitHub, vous devez le suivre sur CircleCI en utilisant le fichier `config.yml` présent dans `.circleci`.  
Il faut maintenant créer une application sur heroku soit sur le site, soit avec la commande :   
`heroku create <nomapp>`   
On vous demandera d'être connecté si ce n'est pas fait :   
`heroku login`  
Sur Circle CI il faudra ajouter quelques variables qui vous seront propres.  
Pour cela allez dans le projet sur CircleCI puis Settings et enfin Environment Variables et ajoutez :
- DOCKER_LOGIN : Votre nom d'utilisateur sur Docker
- DOCKER_PASSWORD : Votre mot de passe sur Docker
- HEROKU_API_KEY : Voir ci-dessous pour l'obtenir
- HEROKU_APP_NAME : Nom de l'application donné plus tôt
- SECRET_KEY : La clé secrète du projet django
- SENTRY_DSN : Le DSN fourni lors de la liaison entre Sentry et notre projet (Voir Surveillance)   

Pour avoir HEROKU_API_KEY :
- soit `heroku authorizations:create` pour la production (par défaut pas d'expiration)
- soit `heroku auth:token` pour le développement (expire au bout d'un an)

La SECRET_KEY est nécessaire pour le déploiement 
(sans celle-ci le pipeline passerait, mais pas lorsque l'on irait sur le site)

Récupération de l'image du registre (Dcoker) :  
`docker run -d -p 8000:8000 <imagedocker>`  

Pour voir si tout est bon pour le deploiement : 
`heroku run python manage.py check --deploy -a <nomappheroku>`
Vous pouvez ensuite vous rendre à l'adresse `http://127.0.0.1:8000/`    

#### Surveillance
Utilisation de Sentry :  
Il faut au préalable lancer le projet avec `python3 manage.py runserver`    
Ensuite après avoir créé un compte sur Sentry: `https://sentry.io/signup/`  
Aller dans la partie Projects puis Create Projects  
A ce moment-là on vous donnera du code à écrire (ne le faite pas tout est fait)
conservez seulement le DSN et mettez-le dans la variable SENTRY_DSN.  
Si vous vous êtes trompé, vous pouvez le récupérer 
 en allant dans Settings --> Projects --> Client keys  

Petit + :  
Un DSN (Data Source Name) est une structure de donnée utilisée pour décrire une connexion à une source de donnée.  
Dans le cas de Sentry il est sous la forme : {PROTOCOL}://{PUBLIC_KEY}:{SECRET_KEY}@{HOST}{PATH}/{PROJECT_ID}  
