# Generated by Django 2.2.4 on 2019-10-20 07:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landslide_a', '0012_about_link_to_website'),
    ]

    operations = [
        migrations.AddField(
            model_name='articles',
            name='text_ua',
            field=models.TextField(default='Введіть текст'),
        ),
        migrations.AddField(
            model_name='articles',
            name='title_ua',
            field=models.CharField(default='Введіть заголовк статті', max_length=1000),
        ),
        migrations.AddField(
            model_name='event',
            name='main_text_ua',
            field=models.TextField(default='Введіть текст', max_length=10000),
        ),
        migrations.AddField(
            model_name='event',
            name='title_ua',
            field=models.TextField(default='Введіть заголовок', max_length=100),
        ),
        migrations.AddField(
            model_name='event',
            name='type_of_event_ua',
            field=models.TextField(default='Введіть тип події'),
        ),
        migrations.AddField(
            model_name='main_block',
            name='first_block_text_ua',
            field=models.TextField(default='Текст першого блоку'),
        ),
        migrations.AddField(
            model_name='main_block',
            name='first_block_title_ua',
            field=models.TextField(default='Заголовок першого блоку'),
        ),
        migrations.AddField(
            model_name='main_block',
            name='second_block_text_ua',
            field=models.TextField(default='Текст другого блоку'),
        ),
        migrations.AddField(
            model_name='main_block',
            name='second_block_title_ua',
            field=models.TextField(default='Заголовок другого блоку'),
        ),
        migrations.AddField(
            model_name='person',
            name='first_name_ua',
            field=models.TextField(default="Введіть ім'я"),
        ),
        migrations.AddField(
            model_name='person',
            name='last_name_ua',
            field=models.TextField(default='Введіть прізвище'),
        ),
        migrations.AlterField(
            model_name='articles',
            name='text',
            field=models.TextField(default='Enter text here'),
        ),
    ]