# Generated by Django 4.2 on 2024-11-16 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hollymagazines', '0002_publicatie_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='publicatie',
            name='description',
            field=models.TextField(default='', editable=False),
        ),
    ]