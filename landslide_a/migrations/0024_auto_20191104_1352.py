# Generated by Django 2.2.4 on 2019-11-04 11:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0023_auto_20191104_1247'),
    ]

    operations = [
        migrations.AlterField(
            model_name='form_user1',
            name='last_name',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='form_user1',
            name='mail',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='form_user1',
            name='name',
            field=models.TextField(default=None),
        ),
        migrations.AlterField(
            model_name='form_user1',
            name='phone',
            field=models.IntegerField(default=None),
        ),
    ]
