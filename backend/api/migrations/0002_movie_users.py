# Generated by Django 2.2.4 on 2019-08-20 01:35

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='movies', to=settings.AUTH_USER_MODEL),
        ),
    ]