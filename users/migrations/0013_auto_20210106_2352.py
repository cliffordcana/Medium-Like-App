# Generated by Django 2.2.13 on 2021-01-06 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_delete_profile'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='full_name',
            field=models.CharField(max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='picture',
            field=models.ImageField(default='default.jpg', max_length=225, upload_to='profile_pics'),
        ),
    ]
