# Generated by Django 4.1.7 on 2023-04-17 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('deals', '0011_alter_deal_club_member_discount_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deal',
            name='club_member_discount_type',
            field=models.CharField(choices=[('fixed', 'Fixed Amount'), ('percentage', 'Percentage Off')], max_length=20, null=True, verbose_name='Discount Type'),
        ),
    ]
