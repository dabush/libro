# Generated by Django 2.1 on 2018-09-06 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0023_auto_20180904_2152'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('slug', models.SlugField()),
            ],
        ),
        migrations.CreateModel(
            name='ListEntry',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='book',
            name='likes',
        ),
        migrations.AddField(
            model_name='listentry',
            name='book',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_list', to='books.Book'),
        ),
        migrations.AddField(
            model_name='listentry',
            name='book_list',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='in_list', to='books.BookList'),
        ),
        migrations.AddField(
            model_name='book',
            name='lists',
            field=models.ManyToManyField(related_name='book_lists', through='books.ListEntry', to='books.BookList'),
        ),
    ]
