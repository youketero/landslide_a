# Generated by Django 2.2.4 on 2019-09-09 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0011_event_location'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='link_to_website',
            field=models.TextField(default='enter e-mail here', max_length=100),
        ),
    ]
