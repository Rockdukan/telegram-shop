# Generated by Django 3.2.8 on 2023-12-25 20:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_auto_20211123_0051'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageset',
            name='content_type',
        ),
        migrations.RemoveField(
            model_name='imageset',
            name='object_id',
        ),
    ]