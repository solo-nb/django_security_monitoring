import os
from dotenv import load_dotenv
from environs import Env


load_dotenv()
env = Env()

DATABASES = {
    'default': {
        'ENGINE': env.str('DSM_ENGINE'),
        'HOST': env.str('DSM_HOST'),
        'PORT': env.str('DSM_PORT'),
        'NAME': env.str('DSM_NAME'),
        'USER': env.str('DSM_USER'),
        'PASSWORD': env.str('DSM_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('DSM_SECRET_KEY')

DEBUG = env.bool('DEBUG')

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
    },
]


USE_L10N = True

LANGUAGE_CODE = 'ru-ru'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'
