# Generated by Django 4.1.7 on 2023-04-08 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0020_alter_location_city_alter_location_country_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='city',
            field=models.CharField(max_length=30, verbose_name='City'),
        ),
        migrations.AlterField(
            model_name='location',
            name='country',
            field=models.CharField(max_length=20, verbose_name='Country'),
        ),
        migrations.AlterField(
            model_name='location',
            name='state',
            field=models.CharField(max_length=30, verbose_name='State'),
        ),
    ]
