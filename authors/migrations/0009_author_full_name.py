# Generated by Django 2.1 on 2018-09-01 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors', '0008_author_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='full_name',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
