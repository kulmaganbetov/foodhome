# Generated by Django 3.1.4 on 2021-02-08 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site_food', '0010_good_is_slider'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='good',
            name='is_recommended',
        ),
        migrations.RemoveField(
            model_name='good',
            name='is_slider',
        ),
        migrations.AddField(
            model_name='category',
            name='is_slider',
            field=models.BooleanField(default=False),
        ),
    ]
