# Generated by Django 2.2.13 on 2020-12-25 08:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0002_articles_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=40)),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='categories', to='articles.Articles')),
            ],
            options={
                'verbose_name_plural': 'categories',
            },
        ),
    ]
