# Generated by Django 4.1.7 on 2023-04-05 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0012_myuser_ngo'),
    ]

    operations = [
        migrations.AddField(
            model_name='planfeature',
            name='numbers_allowed',
            field=models.IntegerField(default=0),
        ),
    ]
