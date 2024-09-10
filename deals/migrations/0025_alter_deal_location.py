# Generated by Django 4.1.7 on 2023-07-18 11:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0092_alter_currency_sign'),
        ('deals', '0024_alter_propertydetails_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='location',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='location_deal', to='account.location'),
        ),
    ]
