# Generated by Django 2.0.1 on 2018-08-22 18:47

from django.db import migrations
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='country',
            field=django_countries.fields.CountryField(max_length=2),
        ),
    ]
