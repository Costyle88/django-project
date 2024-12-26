# Generated by Django 4.2.4 on 2024-12-26 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('viewer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MovieActor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=100)),
                ('actor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.actor')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='viewer.movie')),
            ],
        ),
    ]
