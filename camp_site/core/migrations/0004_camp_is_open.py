# Generated by Django 3.1.5 on 2021-01-13 04:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_remove_camp_number_campers'),
    ]

    operations = [
        migrations.AddField(
            model_name='camp',
            name='is_open',
            field=models.BooleanField(default=True),
        ),
    ]
