# Generated by Django 4.1.7 on 2023-09-01 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0135_rename_provider_type_myuser_service_provider_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='reservation_walkin',
            field=models.CharField(choices=[('reservation', 'Need Reservation'), ('walkin', 'Walkin Allowed')], max_length=16, null=True),
        ),
    ]
