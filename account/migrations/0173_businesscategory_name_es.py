# Generated by Django 4.1.7 on 2024-03-06 10:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0172_stripepaymentmethod_is_default_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='businesscategory',
            name='name_es',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
