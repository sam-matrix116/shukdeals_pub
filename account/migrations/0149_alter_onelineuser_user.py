# Generated by Django 4.1.7 on 2023-09-13 05:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0148_onelineuser'),
    ]

    operations = [
        migrations.AlterField(
            model_name='onelineuser',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='online_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
