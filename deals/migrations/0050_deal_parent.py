# Generated by Django 4.1.7 on 2023-10-30 11:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0049_deal_all_stores'),
    ]

    operations = [
        migrations.AddField(
            model_name='deal',
            name='parent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='deals.deal'),
        ),
    ]
