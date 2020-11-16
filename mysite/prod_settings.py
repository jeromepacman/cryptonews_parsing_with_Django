import dj_database_url

from mysite.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['cryptonews.herokuapp.com']

SECURE_SSL_REDIRECT = True

DATABASES['default'] = dj_database_url.config(conn_max_age=500)
