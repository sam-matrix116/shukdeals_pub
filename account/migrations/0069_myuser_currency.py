# Generated by Django 4.1.7 on 2023-06-21 11:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0068_remove_myuser_currency_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='currency',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_currency', to='account.currency'),
        ),
    ]
