# Generated by Django 2.2.4 on 2019-09-04 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0010_auto_20190904_2058'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.TextField(default='Write location heres'),
        ),
    ]
