# Generated by Django 3.1 on 2020-09-09 02:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0007_auto_20200909_0027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='list_date',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 9, 9, 2, 30, 42, 261372, tzinfo=utc)),
        ),
    ]
