# Generated by Django 3.1.5 on 2021-01-14 04:10

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20210114_0409'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='end_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
        migrations.AddField(
            model_name='event',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
