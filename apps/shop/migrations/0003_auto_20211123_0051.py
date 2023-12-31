# Generated by Django 3.2.8 on 2021-11-22 21:51

import apps.shop.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0002_auto_20211111_1059'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageset',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=apps.shop.models.product_directory_path),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='products/', verbose_name='Основное изображение'),
        ),
    ]
