# MySQL settings
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'NAME': 'DB_Name',
        'USER': 'LOGIN',
        'PASSWORD': 'PaSsWoRd',
        'OPTIONS': {'init_command': "SET sql_mode='STRICT_TRANS_TABLES'",},
        'CONN_MAX_AGE': 60 * 10,  # 10 minutes
    }
}
