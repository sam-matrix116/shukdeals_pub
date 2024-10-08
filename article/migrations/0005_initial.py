# Generated by Django 4.1.7 on 2023-05-30 05:03

import article.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0066_myuser_favourite_job'),
        ('article', '0004_delete_news'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to=article.models.news_pic_path)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='account.businesscategory')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='user_articles', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
