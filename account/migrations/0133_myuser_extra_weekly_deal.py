# Generated by Django 4.1.7 on 2023-08-30 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0132_remove_transaction_stripe_remove_transaction_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='extra_weekly_deal',
            field=models.BooleanField(default=False),
        ),
    ]
