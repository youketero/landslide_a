# Generated by Django 2.2.4 on 2019-11-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0020_main_object_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='main_object',
            name='type_ua',
            field=models.TextField(default=''),
        ),
    ]
