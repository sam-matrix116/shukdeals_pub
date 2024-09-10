# Generated by Django 4.1.7 on 2023-04-11 03:41

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0033_alter_ngovideo_users_liked'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ngovideo',
            name='users_liked',
            field=models.ManyToManyField(blank=True, related_name='users_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
