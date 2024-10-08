# Generated by Django 4.1.7 on 2023-06-28 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0078_stripedetail_cancellation_reason_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stripedetail',
            name='status',
            field=models.CharField(choices=[('pending', 'Pending'), ('complete', 'Complete'), ('cancelled', 'Cancelled')], default='pending', max_length=20),
        ),
    ]
