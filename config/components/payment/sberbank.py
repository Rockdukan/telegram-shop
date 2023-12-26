"""Sberbank settings"""


MERCHANTS = {
    %merchant_id%: {
        'username': '%merchant_username%',
        'password': '%merchant_password%',
        # перенаправление после успешного платежа
        'success_url': 'http://ваш.домен/sberbank/payment/success',
        # перенаправление после неуспешного платежа
        'fail_url': 'http://ваш.домен/sberbank/payment/fail',
        #  это URL, с помощью которого приложение может среагировать
        #  на успешный платеж после того, как отработает коллбэк success_url
        'app_success_url': 'http://ваш.домен/payment/success',
        # это URL, с помощью которого приложение может среагировать на
        # неуспешный платеж после того, как отработает коллбэк fail_url
        'app_fail_url': 'http://ваш.домен/payment/fail',
    }
}

ENVIRONMENT = "production"
