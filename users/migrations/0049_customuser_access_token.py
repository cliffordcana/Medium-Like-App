# Generated by Django 2.2.13 on 2021-01-10 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0048_auto_20210110_2137'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='access_token',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
