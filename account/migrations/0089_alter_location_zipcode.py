# Generated by Django 4.1.7 on 2023-07-05 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0088_myuser_extra_classified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='zipcode',
            field=models.CharField(max_length=12, verbose_name='Zipcode'),
        ),
    ]
