# Generated by Django 4.1.7 on 2023-04-17 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0008_alter_deal_expiry_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='status',
            field=models.CharField(choices=[('active', 'Active'), ('payment_pending', 'Payment Pending')], default='payment_pending', max_length=20),
        ),
    ]
