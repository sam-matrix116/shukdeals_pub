# Generated by Django 4.1.7 on 2023-04-06 06:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0016_plan_donation_plan_platform'),
    ]

    operations = [
        migrations.RenameField(
            model_name='plan',
            old_name='platform',
            new_name='shuk_tv',
        ),
    ]
