# Generated by Django 2.2.13 on 2021-01-01 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_auto_20210101_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articles',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
