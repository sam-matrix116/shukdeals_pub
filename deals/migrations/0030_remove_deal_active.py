# Generated by Django 4.1.7 on 2023-07-20 06:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0029_alter_deal_active'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='deal',
            name='active',
        ),
    ]
