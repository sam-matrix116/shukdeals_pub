# Generated by Django 4.1.7 on 2023-04-17 11:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0043_ngoreferaltoken'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='plan',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.plan'),
        ),
    ]
