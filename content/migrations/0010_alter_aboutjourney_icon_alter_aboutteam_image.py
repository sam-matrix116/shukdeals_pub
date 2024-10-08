# Generated by Django 4.1.7 on 2023-09-12 12:50

import content.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0009_contactus'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aboutjourney',
            name='icon',
            field=models.ImageField(max_length=256, upload_to=content.models.aboutus_pictures_path),
        ),
        migrations.AlterField(
            model_name='aboutteam',
            name='image',
            field=models.ImageField(max_length=256, upload_to=content.models.aboutus_pictures_path),
        ),
    ]
