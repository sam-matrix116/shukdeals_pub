# Generated by Django 4.1.7 on 2023-05-30 07:24

import article.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0007_alter_news_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='image',
            field=models.ImageField(upload_to=article.models.news_pic_path),
        ),
    ]
