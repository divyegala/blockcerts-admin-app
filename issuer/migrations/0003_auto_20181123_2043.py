# Generated by Django 2.1.3 on 2018-11-23 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('issuer', '0002_auto_20181123_2039'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='add_issuer_timestamp',
            field=models.DateTimeField(default='2018-11-23 00:00'),
        ),
    ]