# Generated by Django 4.1.7 on 2023-06-28 05:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0076_alter_stripedetail_payment_method'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripedetail',
            name='amount',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='stripedetail',
            name='currency',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='stripedetail',
            name='item_type',
            field=models.CharField(choices=[('plan', 'Plan')], default='plan', max_length=20),
        ),
    ]
