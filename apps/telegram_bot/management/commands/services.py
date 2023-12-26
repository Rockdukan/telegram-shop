from django.core.exceptions import ObjectDoesNotExist

from apps.shop.models import *
from apps.telegram_bot.models import *


def check_cart(user):
    try:
        carts = Cart.objects.filter(user=user)
        cart = carts.get(in_order=False)
    except ObjectDoesNotExist:
        cart = Cart.objects.create(user=user)
    return cart


def check_product_in_cart(cart, product):
    products_in_cart = CartProduct.objects.filter(cart=cart)
    for product_in_car in products_in_cart:
        if product_in_car.product == product:
            product_in_car.qty += 1
            product_in_car.save()
            return True
    return False


def check_user(telegram_user_id):
    try:
        user = TelegramUser.objects.get(telegram_user_id=telegram_user_id)
    except ObjectDoesNotExist:
        user = TelegramUser.objects.create(telegram_user_id=telegram_user_id)
    check_cart(user)
    return user


def get_cart_products(cart):
    products = CartProduct.objects.filter(cart=cart)
    return products
