# Generated by Django 2.2.13 on 2021-01-08 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_auto_20210108_1117'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='first_name',
        ),
        migrations.AddField(
            model_name='customuser',
            name='first_ame',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
