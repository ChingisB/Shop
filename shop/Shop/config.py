# SECURITY WARNING: keep the secret key used in production secret!
import dj_database_url
import os


SECRET_KEY = 'django-insecure-y(fj+qvk13mts54cro*6wd*w20axz+0-oe@hp38)j+r!_gacxr'
DATABASES = {
    'default': dj_database_url.config(
        default=os.environ.get("DATABASE_URL")
    )
}

IMAGE_SERVICE = os.environ.get("IMAGE_SERVICE")
