# Generated by Django 2.2.4 on 2019-11-01 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0016_foto_news_geological_background_geological_objects'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='cur_pos',
            field=models.TextField(default='Enter position'),
        ),
        migrations.AddField(
            model_name='person',
            name='cur_pos_ua',
            field=models.TextField(default='Enter position'),
        ),
    ]