# Generated by Django 2.1.3 on 2018-11-24 01:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0003_auto_20181123_2043'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='add_issuer_timestamp',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 24, 1, 15, 53, 809702)),
        ),
        migrations.AlterField(
            model_name='person',
            name='public_address',
            field=models.CharField(default='', max_length=250),
        ),
    ]