# Generated by Django 4.1.7 on 2023-04-14 10:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0007_alter_deal_club_member_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='expiry_date',
            field=models.DateField(),
        ),
    ]
