# Generated by Django 2.2.13 on 2021-01-10 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0045_auto_20210110_1509'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(upload_to='images'),
        ),
    ]
