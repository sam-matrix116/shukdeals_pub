# Generated by Django 4.1.7 on 2023-08-14 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0121_stripedetailnew_amount_stripedetailnew_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='tranzilatoken',
            name='card_mask',
            field=models.CharField(max_length=30, null=True),
        ),
    ]
