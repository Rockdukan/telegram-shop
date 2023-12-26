""" SMTP settings """


ADMINS = (
    ('admin', 'admin@example.com'),
)

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"

EMAIL_HOST = "mail.hosting.reg.ru"

EMAIL_HOST_USER = "activ@kaoso.online"

EMAIL_HOST_PASSWORD = "AbraKadabra1!"

EMAIL_PORT = 587

EMAIL_SUBJECT_PREFIX = ''

EMAIL_USE_SSL = False

EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = EMAIL_HOST_USER

SERVER_EMAIL = EMAIL_HOST_USER


