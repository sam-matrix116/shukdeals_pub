# Generated by Django 4.1.7 on 2023-06-22 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0071_alter_myuser_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='stripe_customer_id',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
