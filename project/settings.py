import os
from dotenv import load_dotenv
load_dotenv()

DATABASES = {
    'default': {
        'ENGINE': os.getenv('DSM_ENGINE'),
        'HOST': os.getenv('DSM_HOST'),
        'PORT': os.getenv('DSM_PORT'),
        'NAME': os.getenv('DSM_NAME'),
        'USER': os.getenv('DSM_USER'),
        'PASSWORD': os.getenv('DSM_PASSWORD'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = os.getenv('DSM_SECRET_KEY')

DEBUG = (
    os.getenv('DSM_DEBUG') == 'TRUE' 
    or os.getenv('DSM_DEBUG') == 'True' 
    or os.getenv('DSM_DEBUG') == 'true'
)

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['*']


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
