# Generated by Django 2.2.13 on 2021-01-09 03:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_auto_20210108_1439'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='customuser',
            table='users_customuser',
        ),
    ]