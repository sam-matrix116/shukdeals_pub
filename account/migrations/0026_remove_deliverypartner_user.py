# Generated by Django 4.1.7 on 2023-04-08 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0025_alter_myuser_business_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deliverypartner',
            name='user',
        ),
    ]
