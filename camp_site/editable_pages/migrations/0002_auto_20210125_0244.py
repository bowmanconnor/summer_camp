# Generated by Django 3.1.5 on 2021-01-25 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editable_pages', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='home',
            name='title_image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
