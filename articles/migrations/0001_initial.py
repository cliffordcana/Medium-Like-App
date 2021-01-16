# Generated by Django 2.2.13 on 2020-12-25 08:17

import articles.models
from django.db import migrations, models
import image_cropping.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.TextField()),
                ('slug', models.SlugField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to=articles.models.upload_dir_path)),
                ('cropping', image_cropping.fields.ImageRatioField('image', '1000x1000', adapt_rotation=False, allow_fullsize=False, free_crop=False, help_text=None, hide_image_field=False, size_warning=False, verbose_name='cropping')),
                ('article_choices', models.CharField(choices=[('P', 'Python'), ('D', 'Django'), ('DRF', 'Django Rest Framework'), ('JS', 'Javascript'), ('R', 'React'), ('M', 'MySQL'), ('H', 'HTML'), ('C', 'CSS'), ('RA', 'RELATED_ARTICLES')], default='P', max_length=3)),
            ],
            options={
                'verbose_name_plural': 'articles',
            },
        ),
    ]
