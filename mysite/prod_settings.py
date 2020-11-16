from mysite.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

ALLOWED_HOSTS = ['cryptonews.herokuapp.com']

SECURE_SSL_REDIRECT = True

SECRET_KEY = os.environ['SECRET_KEY']

