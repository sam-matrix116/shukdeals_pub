# Generated by Django 4.1.7 on 2023-05-30 05:02

import article.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='image',
            field=models.ImageField(default=None, null=True, upload_to=article.models.news_pic_path),
        ),
    ]
