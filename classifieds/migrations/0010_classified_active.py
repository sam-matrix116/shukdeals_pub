# Generated by Django 4.1.7 on 2023-04-21 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0009_alter_classified_price_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='classified',
            name='active',
            field=models.BooleanField(default=True),
        ),
    ]
