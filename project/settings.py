import os
import dj_database_url
from dotenv import load_dotenv
from environs import Env, EnvError


load_dotenv()
env = Env()

DSM_DB_URL = env.str('DSM_DB_URL')
db_url = dj_database_url.parse(DSM_DB_URL)
DATABASES = {
    'default': {
        'ENGINE': db_url['ENGINE'],
        'HOST': db_url['HOST'],
        'PORT': db_url['PORT'],
        'NAME': db_url['NAME'],
        'USER': db_url['USER'],
        'PASSWORD': db_url['PASSWORD'],
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = env.str('DSM_SECRET_KEY')

try:
    DEBUG = env.bool('DSM_DEBUG')
except EnvError:
    DEBUG = False

ROOT_URLCONF = 'project.urls'

try:
    ALLOWED_HOSTS = env.list('DSM_ALLOWED_HOSTS')
except EnvError:
    ALLOWED_HOSTS = ['localhost', '127.0.0.1']


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
