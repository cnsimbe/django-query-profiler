import os

from django_query_profiler.settings import *

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


INSTALLED_APPS = (
    'django_query_profiler',
    'tests.testapp',
)

SECRET_KEY = 'dummy'

ROOT_URLCONF = 'tests.testapp.urls'

DATABASES = {
    'default': {
        'ENGINE': 'django_query_profiler.django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

MIDDLEWARE = [
    # __ADDED FOR DJANGO QUERY PROFILER __
    'django_query_profiler.client.middleware.QueryProfilerMiddleware',
]