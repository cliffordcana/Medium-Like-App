# Generated by Django 2.2.13 on 2021-01-08 03:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0021_auto_20210108_1122'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='picture',
            new_name='picture_url',
        ),
    ]
