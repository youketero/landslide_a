# Generated by Django 2.2.4 on 2019-08-17 17:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0002_auto_20190816_2106'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='short',
            field=models.TextField(default='enter please'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='title',
            field=models.CharField(max_length=1000),
        ),
    ]
