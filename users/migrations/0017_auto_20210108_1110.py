# Generated by Django 2.2.13 on 2021-01-08 03:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_auto_20210108_1107'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='picture_url',
            new_name='picture',
        ),
    ]
