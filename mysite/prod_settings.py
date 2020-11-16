from mysite.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = get_env_variable('SECRET_KEY')

ALLOWED_HOSTS = ['cryptonews.herokuapp.com', 'www.cryptonews.herokuapp']

SECURE_SSL_REDIRECT = True


