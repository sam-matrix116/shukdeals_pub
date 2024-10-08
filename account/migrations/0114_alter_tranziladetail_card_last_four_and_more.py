# Generated by Django 4.1.7 on 2023-08-05 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0113_tranziladetail_error_code_tranziladetail_error_info'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tranziladetail',
            name='card_last_four',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='card_locality',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='card_mask',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='credit_card_owner_id',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='currency_code',
            field=models.CharField(max_length=2, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='expiry_month',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='expiry_year',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='payment_plan',
            field=models.CharField(max_length=4, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='processor_response_code',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='token',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='tranmode',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='tranziladetail',
            name='txn_type',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
