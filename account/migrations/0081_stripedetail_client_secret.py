# Generated by Django 4.1.7 on 2023-06-29 06:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0080_transaction'),
    ]

    operations = [
        migrations.AddField(
            model_name='stripedetail',
            name='client_secret',
            field=models.TextField(null=True),
        ),
    ]
