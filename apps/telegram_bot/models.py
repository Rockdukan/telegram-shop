from django.db import models

from apps.shop.models import Product


class TelegramUser(models.Model):
    """ Пользователь """
    telegram_user_id = models.PositiveIntegerField('ID пользователя')

    class Meta:
        ordering = ('telegram_user_id',)
        verbose_name = 'Пользователь Telegram'
        verbose_name_plural = 'Пользователи Telegram'

    def __str__(self):
        return str(self.telegram_user_id)


class Address(models.Model):
    """ Адрес """
    user = models.ForeignKey(
        'TelegramUser',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Покупатель')
    country = models.CharField('Страна', max_length=255)
    city = models.CharField('Город', max_length=255)
    street = models.CharField('Улица', max_length=255)
    room = models.CharField('Клмната', max_length=255)
    post_code = models.CharField('Индекс', max_length=255)
    mobile = models.CharField('Телефон', max_length=255)

    class Meta:
        verbose_name = 'Адрес'
        verbose_name_plural = 'Адреса покупателей'


class CartProduct(models.Model):
    """ Товары в корзине """
    user = models.ForeignKey(
        'TelegramUser',
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Покупатель')
    cart = models.ForeignKey(
        'Cart',
        on_delete=models.CASCADE,
        related_name='related_products',
        verbose_name='Корзина')
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Товар')
    qty = models.PositiveIntegerField(
        default=1,
        verbose_name='Кол-во')
    final_price = models.DecimalField(
        decimal_places=2,
        max_digits=9,
        verbose_name='Общая цена')

    class Meta:
        verbose_name = 'Корзина с продуктом'
        verbose_name_plural = 'Корзины с продуктами'

    def __str__(self):
        return f'Пользователь: {self.user} Корзина: {self.cart.id} Продукт: {self.product.title}(ID:{self.product.id}) Кол-во:{self.qty}'

    def save(self, *args, **kwargs):
        self.final_price = self.qty * self.product.price
        super().save(*args, **kwargs)


class Cart(models.Model):
    """ Корзина """
    user = models.ForeignKey(
        'TelegramUser',
        blank=True,
        null=True,
        on_delete=models.CASCADE)
    products = models.ManyToManyField(
        CartProduct,
        blank=True,
        related_name='related_cart')
    total_products = models.PositiveIntegerField(default=0)
    in_order = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Корзина'
        verbose_name_plural = 'Корзины'

    def __str__(self):
        return f'{self.user} - {self.in_order}'

    def get_final_price(self):
        products = CartProduct.objects.filter(cart=self)
        final_price = 0

        for product in products:
            final_price += product.final_price
        
        return final_price


class Order(models.Model):
    """ Заказ """
    customer = models.ForeignKey(
        TelegramUser,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        related_name='related_orders',
        verbose_name='Покупатель')
    cart = models.ForeignKey(
        Cart,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Корзина')
    created_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Дата создания заказа')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return f'{self.customer} - {self.created_at}'
