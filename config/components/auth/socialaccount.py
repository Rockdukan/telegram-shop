"""Socialaccount settings"""


# Указывает используемый класс адаптера, позволяющий изменять
# определенное поведение по умолчанию.
SOCIALACCOUNT_ADAPTER = 'allauth.socialaccount.adapter.DefaultSocialAccountAdapter'

# Попытайтесь обойти форму регистрации, используя поля
# (например, имя пользователя, адрес электронной почты),
# полученные от поставщика социальной учетной записи.
# Если возникнет конфликт из-за дубликата адреса электронной почты,
# форма регистрации все равно сработает.
SOCIALACCOUNT_AUTO_SIGNUP = True

# Подтверждение электронной почты для социальных аккаунтов.
SOCIALACCOUNT_EMAIL_VERIFICATION = 'none'  # none | mandatory | optional
# Пользователь обязан передать адрес электронной почты при регистрации
# с помощью социальной учетной записи.
SOCIALACCOUNT_EMAIL_REQUIRED = False

# Используется для переопределения формы,
# например: {'signup': 'myapp.forms.SignupForm'}
SOCIALACCOUNT_FORMS = {}

# При регистрации пользователь обязан указать адрес электронной почты соц.сети
# Например используя OpenID AX или Facebook “email” permission.
SOCIALACCOUNT_QUERY_EMAIL = False

# Указывает, хранятся ли токены доступа в базе данных
SOCIALACCOUNT_STORE_TOKENS = True
