# Generated by Django 3.1 on 2020-09-07 14:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Realtor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=100)),
                ('is_mvp', models.BooleanField(default=True)),
                ('hire_date', models.DateTimeField(blank=True, default=datetime.datetime(2020, 9, 7, 14, 15, 20, 434789))),
                ('photo', models.ImageField(blank=True, upload_to='upload/%Y/%m/%d/')),
            ],
        ),
    ]
