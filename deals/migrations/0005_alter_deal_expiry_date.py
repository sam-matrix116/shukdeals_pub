# Generated by Django 4.1.7 on 2023-04-14 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0004_deal_expiry_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='expiry_date',
            field=models.DateTimeField(),
        ),
    ]
