# Generated by Django 3.1 on 2020-09-09 00:27

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0006_auto_20200908_1041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 9, 0, 27, 27, 537566, tzinfo=utc)),
        ),
    ]
