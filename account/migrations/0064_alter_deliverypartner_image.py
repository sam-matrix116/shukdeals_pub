# Generated by Django 4.1.7 on 2023-05-22 06:38

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0063_deliverypartner_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deliverypartner',
            name='image',
            field=models.ImageField(null=True, upload_to=account.models.delivery_partners_path),
        ),
    ]
