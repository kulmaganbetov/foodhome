# Generated by Django 3.1.4 on 2021-02-19 08:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('construct_site', '0005_support_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phonenumber',
            name='last_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
