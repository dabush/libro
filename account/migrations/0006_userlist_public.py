# Generated by Django 2.1 on 2018-09-12 01:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20180911_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='userlist',
            name='public',
            field=models.BooleanField(default=True),
        ),
    ]
