# Generated by Django 3.1.8 on 2021-08-10 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('que_slug', models.CharField(default='', max_length=300)),
                ('answer', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Cantact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('email_address', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cat_slug', models.CharField(default='', max_length=300)),
                ('Que_title', models.CharField(max_length=50)),
                ('Que_desc', models.TextField()),
                ('slug', models.SlugField(blank=True, null=True, unique=True)),
            ],
        ),
    ]
