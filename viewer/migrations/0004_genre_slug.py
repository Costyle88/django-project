# Generated by Django 4.2 on 2024-11-10 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0003_movie_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='genre',
            name='slug',
            field=models.SlugField(default='', editable=False, unique=True),
        ),
    ]
