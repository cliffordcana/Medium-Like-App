# Generated by Django 2.2.13 on 2021-01-08 03:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0022_auto_20210108_1124'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='public_profile',
            field=models.ImageField(default='default.jpg', max_length=225, upload_to='profile_pics'),
        ),
    ]
