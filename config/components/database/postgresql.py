# PostgeSQL settings
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': '127.0.0.1',
        'PORT': '5432',
        'NAME': 'DB_Name',
        'USER': 'LOGIN',
        'PASSWORD': 'PaSsWoRd',
        'CONN_MAX_AGE': 60 * 10,  # 10 minutes
    }
}
