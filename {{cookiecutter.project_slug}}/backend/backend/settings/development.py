# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/
from .base import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ')w4vem*wxv2y(qp+*p)m(1ko496-)4473w08!=-hf2vkuq5tbr'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    "backend",
]

INSTALLED_APPS += [
    'django_extensions',
]
