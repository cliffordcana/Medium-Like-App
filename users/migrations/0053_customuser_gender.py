# Generated by Django 2.2.13 on 2021-01-11 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0052_auto_20210111_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
