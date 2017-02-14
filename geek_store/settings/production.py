import dj_database_url
from django.conf import settings

DEBUG = False

DATABASE = settings.DATABASE

db_from_env = dj_database_url.config(conn_max_age=500)

DATABASE['default'].update(db_from_env)

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFileStorage'
