# Generated by Django 4.1.7 on 2023-04-08 04:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_alter_location_address_alter_location_latitude_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='latitude',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
        migrations.AlterField(
            model_name='location',
            name='location',
            field=models.TextField(blank=True, null=True, verbose_name='Property Location'),
        ),
        migrations.AlterField(
            model_name='location',
            name='longitude',
            field=models.DecimalField(decimal_places=3, max_digits=8),
        ),
    ]
