# Generated by Django 3.1.5 on 2021-01-12 22:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_camp_number_campers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='camp',
            name='number_campers',
        ),
    ]
