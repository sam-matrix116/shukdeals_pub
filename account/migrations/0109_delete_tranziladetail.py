# Generated by Django 4.1.7 on 2023-08-03 04:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0108_stripedetailnew_payment_detail_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='TranzilaDetail',
        ),
    ]
