# settings/local.py
import os
from dotenv import load_dotenv
from .base import *
load_dotenv()

DEBUG = True

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql_psycopg2",
        "NAME": "eristatistics_local",
        "USER": "postgres",
        "PASSWORD": "123456",
        "HOST": "localhost",
        "PORT": "5432",
    }
}


EMAIL_HOST = "smtp.googlemail.com"
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get("MAIL_USERNAME")
EMAIL_HOST_PASSWORD = os.environ.get("MAIL_PASSWORD")
EMAIL_USE_TLS = True

# INSTALLED_APPS += ("debug_toolbar", )