# Generated by Django 4.1.7 on 2023-10-01 06:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0154_tranziladetail_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='tranziladetail',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='tranzila_detail', to=settings.AUTH_USER_MODEL),
        ),
    ]
