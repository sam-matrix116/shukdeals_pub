# Generated by Django 4.1.7 on 2023-09-25 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0046_deal_is_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='online_supported',
            field=models.BooleanField(default=True),
        ),
    ]
