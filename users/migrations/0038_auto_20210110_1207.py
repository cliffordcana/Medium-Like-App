# Generated by Django 2.2.13 on 2021-01-10 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0037_auto_20210110_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='profile_pics/default.jpg', max_length=225, upload_to='profile_pics'),
        ),
    ]
