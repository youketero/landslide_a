# Generated by Django 2.2.4 on 2019-10-20 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0013_auto_20191020_1017'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='text_ua',
            field=models.TextField(default='Текст', max_length=100000),
        ),
        migrations.AddField(
            model_name='about',
            name='title_ua',
            field=models.TextField(default='Заголовок', max_length=1000),
        ),
    ]
