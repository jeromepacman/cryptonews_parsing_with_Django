
from mysite.settings import *

DEBUG = False

TEMPLATE_DEBUG = False

SECRET_KEY = os.environ['SECRET_KEY']

ALLOWED_HOSTS = ['cryptonews.herokuapp.com', 'www.cryptonews.herokuapp.com']




