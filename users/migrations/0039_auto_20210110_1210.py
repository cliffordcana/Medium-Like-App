# Generated by Django 2.2.13 on 2021-01-10 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0038_auto_20210110_1207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='default.jpg', max_length=225, upload_to='profile_pics'),
        ),
    ]
