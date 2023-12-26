# Generated by Django 3.2.8 on 2021-11-22 21:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('telegram_bot', '0002_remove_cart_final_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=255, verbose_name='Страна')),
                ('city', models.CharField(max_length=255, verbose_name='Город')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('room', models.CharField(max_length=255, verbose_name='Клмната')),
                ('post_code', models.CharField(max_length=255, verbose_name='Индекс')),
                ('mobile', models.CharField(max_length=255, verbose_name='Телефон')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='telegram_bot.telegramuser', verbose_name='Покупатель')),
            ],
            options={
                'verbose_name': 'Адрес',
                'verbose_name_plural': 'Адреса покупателей',
            },
        ),
    ]