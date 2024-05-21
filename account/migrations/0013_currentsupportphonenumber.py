# Generated by Django 3.1.4 on 2021-01-21 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_auto_20210121_1705'),
    ]

    operations = [
        migrations.CreateModel(
            name='CurrentSupportPhoneNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.phonenumber')),
                ('support', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.support')),
            ],
        ),
    ]