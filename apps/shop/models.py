from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from django.db import models
from django.utils.safestring import mark_safe
from smart_selects.db_fields import ChainedForeignKey


class Category(models.Model):
    """ Категория товара """
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    def get_products(self):
        return Product.objects.filter(category__in=[self.id])

    def get_subcategories(self):
        return Subcategory.objects.filter(category__in=[self.id])

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Subcategory(models.Model):
    """ Подкатегория товара """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='related_subcategory_category',
        verbose_name='Категория')
    title = models.CharField(max_length=255, verbose_name='Название')

    def __str__(self):
        return self.title

    def get_products(self):
        return Product.objects.filter(subcategory__in=[self.id])

    class Meta:
        verbose_name = 'Подкатегория'
        verbose_name_plural = 'Подкатегории'


class Product(models.Model):
    """ Продукт """
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        verbose_name='Категория')
    subcategory = ChainedForeignKey(
        Subcategory,
        chained_field="category",
        chained_model_field="category",
        show_all=False,
        auto_choose=True,
        sort=True)
    title = models.CharField('Название', max_length=255)
    description = models.TextField('Описание')
    price = models.PositiveIntegerField('Цена')
    image = models.ImageField(
        'Основное изображение',
        blank=True,
        null=True,
        upload_to='products/')

    class Meta:
        ordering = ('title',)
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'

    def __str__(self):
        return self.title


def product_directory_path(instance, filename):
        """ Функция получения пути к изображениям товара """
        return f'products_extension/{instance.product.id}/{filename}'


class ImageSet(models.Model):
    """ Модель изображений """
    product = models.ForeignKey(
        Product,
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        verbose_name='Продукт')
    image = models.ImageField(
        blank=True,
        null=True,
        upload_to=product_directory_path)

    class Meta:
        verbose_name = 'Фото к продукту'
        verbose_name_plural = 'Фото к продуктам'

    def image_tag(self):
        if self.image.url:
            return mark_safe(f'<img src={self.image.url} width="120px" height="auto"')
