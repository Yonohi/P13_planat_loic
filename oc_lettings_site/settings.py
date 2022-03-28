import os
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration


sentry_sdk.init(
    dsn=os.getenv('SENTRY_DSN'),
    integrations=[DjangoIntegration()],

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production,
    traces_sample_rate=1.0,

    # If you wish to associate users to errors (assuming you are using
    # django.contrib.auth) you may enable sending PII data.
    send_default_pii=True,

    # By default the SDK will try to use the SENTRY_RELEASE
    # environment variable, or infer a git commit
    # SHA as release, however you may want to set
    # something more human-readable.
    # release="myapp@1.0.0",
)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Ici le second argument est la valeur par défaut (utile en développement)
# on lui donnera une autre valeur en production (voir README)
SECRET_KEY = os.getenv('SECRET_KEY', 'fp$9^593hsriajg$_%=5trot9g!1qa@ew(o-1#@=&4%=hp46(s')

# SECURITY WARNING: don't run with debug turned on in production!
# Astuce: comparaison des string pour obtenir un booléen
DEBUG = os.getenv('DEBUG', 'True') == 'True'

ALLOWED_HOSTS = ['oc-lettings-lp.herokuapp.com', '.localhost', '127.0.0.1', '[::1]']


# Application definition

INSTALLED_APPS = [
    'profiles',
    'lettings',
    'oc_lettings_site.apps.OCLettingsSiteConfig',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'oc_lettings_site.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'oc_lettings_site.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'oc-lettings-site.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/
# Help for static
# https://devcenter.heroku.com/articles/django-assets
# Il est important de créer un répertoire static contenant un fichier
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Extra places for collectstatic to find static files.
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

if DEBUG is False:
    # Le cookie CSRF n’est envoyé que pour des connexions HTTPS
    CSRF_COOKIE_SECURE = True
    # Si True, SecurityMiddleware redirige les requêtes non HTTPS vers HTTPS
    SECURE_SSL_REDIRECT = True
    # Le cookie de session n’est envoyé que pour des connexions HTTPS
    SESSION_COOKIE_SECURE = True
    # Très intéressant, voir:
    # https://docs.djangoproject.com/fr/4.0/ref/middleware/#referrer-policy
    # https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Referrer-Policy
    # Remarque : on peut voir le referer dans l'inspecteur web (réseau et en-tête)
    SECURE_REFERRER_POLICY = 'same-origin'
    # Défini l'en-tête HSTS
    # Refuse les connexions à notre nom de domaine si la connexion n’est pas sécurisée
    # (pour une certaine période de temps)
    # Cela réduit l’exposition à certaines attaques de type « homme du milieu »
    SECURE_HSTS_SECONDS = 60
    # voir :
    # https://docs.djangoproject.com/fr/4.0/ref/middleware/#django.middleware.security.SecurityMiddleware
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
