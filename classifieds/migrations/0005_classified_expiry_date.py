# Generated by Django 4.1.7 on 2023-04-19 07:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classifieds', '0004_alter_classified_contact_phone'),
    ]

    operations = [
        migrations.AddField(
            model_name='classified',
            name='expiry_date',
            field=models.DateField(null=True),
        ),
    ]
