# Generated by Django 2.2.13 on 2021-01-08 03:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0019_auto_20210108_1121'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='first_ame',
            new_name='first_name',
        ),
    ]