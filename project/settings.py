from dotenv import load_dotenv
import os


load_dotenv()

DB_ENGINE = os.environ["ENGINE"]
DB_HOST = os.environ["HOST"]
DB_PORT = os.environ["PORT"]
DB_NAME = os.environ["NAME"]
DB_USER = os.environ["USER"]
DB_PASSWORD = os.environ["PASSWORD"]
DB_SECRET_KEY = os.environ["SECRET_KEY"]
DB_DEBUG = os.environ["DB_DEBUG"]

DATABASES = {
    'default': {
        'ENGINE': DB_ENGINE,
        'HOST': DB_HOST,
        'PORT': DB_PORT,
        'NAME': DB_NAME,
        'USER': DB_USER,
        'PASSWORD': DB_PASSWORD,
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = DB_SECRET_KEY

DEBUG = DB_DEBUG

ROOT_URLCONF = 'project.urls'

ALLOWED_HOSTS = ['127.0.0.1', 'localhost']


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
