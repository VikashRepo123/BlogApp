# Generated by Django 3.1.8 on 2021-08-11 07:00

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0005_post_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.ManyToManyField(related_name='blogpost_like', to=settings.AUTH_USER_MODEL),
        ),
    ]